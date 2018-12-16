# Copyright (c) 2018 by Srinivas Garlapati

"""Marshal utility.
"""
import contextlib
import struct
import sys
import six
import six.moves

from pydis import compatibility as compat 
from pydis.constants import FLAG_REF as REF, MARSHAL_CODES
from pydis.constants import IS_PY2, IS_PY3, MAGIC_NUMBERS, PY_VERSION


# TODO: Add more version compatibilities.
# Python2 intrepreter should be supported.

class _NULL(object):
  """Used internally, e.g. as a sentinel in dictionary entry lists."""
  pass


class Code(object):
  """Version-agnostic types.CodeType."""

  def __init__(self, argcount, kwonlyargcount, nlocals, stacksize, flags, code,
               consts, names, varnames, filename, name, firstlineno, lnotab,
               freevars, cellvars, python_version):

    assert isinstance(nlocals, int)
    assert isinstance(stacksize, int)
    assert isinstance(flags, int)
    assert isinstance(filename, (bytes, six.string_types))
    self.co_argcount = argcount
    self.co_kwonlyargcount = kwonlyargcount
    self.co_nlocals = nlocals
    self.co_stacksize = stacksize
    self.co_flags = flags
    self.co_code = code
    self.co_consts = consts
    self.co_names = names
    self.co_varnames = varnames
    self.co_filename = filename
    self.co_name = name
    self.co_firstlineno = firstlineno
    self.co_lnotab = lnotab
    self.co_freevars = freevars
    self.co_cellvars = cellvars
    self.python_version = python_version  # This field is not in types.CodeType.



class _LoadCode(object):
  """Stateful loader for marshalled files."""

  def __init__(self, data, python_version):
    self.bufstr = data
    self.bufpos = 0
    self.python_version = python_version
    self.refs = []
    self._stringtable = []
    # When running under Python 3 and analyzing Python 2, whether load_string
    # should convert bytes to native strings.
    self._keep_bytes = False

  @contextlib.contextmanager
  def keep_bytes(self):
    old = self._keep_bytes
    self._keep_bytes = True
    yield
    self._keep_bytes = old

  def eof(self):
    """Return True if we reached the end of the stream."""
    return self.bufpos == len(self.bufstr)

  def load(self):
    """Load an encoded Python data structure."""
    c = ord('?')  # make pylint happy
    try:
      c = self._read_byte()
      if c & REF:
        # This element might recursively contain other elements, which
        # themselves store things in the refs table. So we need to determine the
        # index position *before* reading the contents of this element.
        idx = self._reserve_ref()
        result = getattr(self, MARSHAL_CODES[c & ~REF])()
        self.refs[idx] = result
      else:
        result = getattr(self, MARSHAL_CODES[c])()
      return result
    except KeyError:
      raise ValueError('bad marshal code: %r (%02x)' % (chr(c), c))
    except IndexError:
      raise EOFError

  def _read(self, n):
    """Read n bytes as a string."""
    pos = self.bufpos
    self.bufpos += n
    if self.bufpos > len(self.bufstr):
      raise EOFError()
    return self.bufstr[pos : self.bufpos]

  def _read_byte(self):
    """Read an unsigned byte."""
    pos = self.bufpos
    self.bufpos += 1
    return six.indexbytes(self.bufstr, pos)

  def _read_short(self):
    """Read a signed 16 bit word."""
    lo = self._read_byte()
    hi = self._read_byte()
    x = lo | (hi<<8)
    if x & 0x8000:
      # sign extension
      x -= 0x10000
    return x

  def _read_long(self):
    """Read a signed 32 bit word."""
    s = self._read(4)
    b = lambda i: six.indexbytes(s, i)
    x = b(0) | b(1)<<8 | b(2)<<16 | b(3)<<24
    if b(3) & 0x80 and x > 0:
      # sign extension
      x = -((1<<32) - x)
      return int(x)
    else:
      return x

  def _read_long64(self):
    """Read a signed 64 bit integer."""
    s = self._read(8)
    b = lambda i: six.indexbytes(s, i)
    x = (b(0) | b(1)<<8 | b(2)<<16 | b(3)<<24 |
         b(4)<<32 | b(5)<<40 | b(6)<<48 | b(7)<<56)
    if b(7) & 0x80 and x > 0:
      # sign extension
      x = -((1<<64) - x)
    return x

  def _reserve_ref(self):
    """Reserve one entry in the reference table.

    This is done before reading an element, because reading an element and
    all its subelements might change the size of the reference table.

    Returns:
      Reserved index position in the reference table.
    """
    # See r_ref_reserve in Python-3.4/Python/marshal.c
    idx = len(self.refs)
    self.refs.append(None)
    return idx

  # pylint: disable=missing-docstring
  # This is a bunch of small methods with self-explanatory names.

  def load_null(self):
    return _NULL

  def load_none(self):
    return None

  def load_true(self):
    return True

  def load_false(self):
    return False

  def load_stopiter(self):
    return StopIteration

  def load_ellipsis(self):
    return Ellipsis

  def load_int(self):
    return self._read_long()

  def load_int64(self):
    return self._read_long64()

  def load_long(self):
    """Load a variable length integer."""
    size = self._read_long()
    x = 0
    for i in six.moves.range(abs(size)):
      d = self._read_short()
      x |= d<<(i*15)
    return x if size >= 0 else -x

  def load_float(self):
    n = self._read_byte()
    s = self._read(n)
    return float(s)

  def load_binary_float(self):
    binary = self._read(8)
    return struct.unpack('<d', binary)[0]

  def load_complex(self):
    n = self._read_byte()
    s = self._read(n)
    real = float(s)
    n = self._read_byte()
    s = self._read(n)
    imag = float(s)
    return complex(real, imag)

  def load_binary_complex(self):
    binary = self._read(16)
    return complex(*struct.unpack('dd', binary))

  def load_string(self):
    n = self._read_long()
    s = self._read(n)
    if self.python_version[0] >= 3:
      # load_string() loads a bytestring, and in Python 3, str and bytes are
      # different classes.
      s = compat.BytesType(s)
    elif not self._keep_bytes:
      # In Python 2, load_string is used to load both bytestrings and native
      # strings, so we have to specify which we want.
      s = compat.native_str(s)
    return s

  def load_interned(self):
    n = self._read_long()
    s = self._read(n)
    ret = six.moves.intern(compat.native_str(s))
    self._stringtable.append(ret)
    return ret

  def load_stringref(self):
    n = self._read_long()
    return self._stringtable[n]

  def load_unicode(self):
    n = self._read_long()
    s = self._read(n)
    # We need to convert bytes to a unicode string for any of the following:
    # - We are analysing python2 code
    # - We are running in a python3 host
    # If we are analysing python3 code in a python2 host, we leave the string as
    # a utf-8 encoded bytestring.
    if (self.python_version[0] < 3 or
        sys.version_info[0] == 3):
      s = s.decode('utf8')
    if self.python_version[0] < 3:
      # In Python 2, unicode and str are different classes.
      s = compat.UnicodeType(s)
    return s

  def load_ascii(self):
    n = self._read_long()
    return compat.native_str(self._read(n))

  def load_short_ascii(self):
    n = self._read_byte()
    return compat.native_str(self._read(n))

  def load_tuple(self):
    return tuple(self.load_list())

  def load_small_tuple(self):
    n = self._read_byte()
    l = []
    for _ in six.moves.range(n):
      l.append(self.load())
    return tuple(l)

  def load_list(self):
    n = self._read_long()
    l = []
    for _ in six.moves.range(n):
      l.append(self.load())
    return l

  def load_dict(self):
    d = {}
    while True:
      key = self.load()
      if key is _NULL:
        break
      value = self.load()
      d[key] = value
    return d

  def load_code(self):
    """Load a Python code object."""
    argcount = self._read_long()
    if self.python_version[0] >= 3:
      kwonlyargcount = self._read_long()
    else:
      kwonlyargcount = -1
    nlocals = self._read_long()
    stacksize = self._read_long()
    flags = self._read_long()
    with self.keep_bytes():
      # The code field is a 'string of raw compiled bytecode'
      # (https://docs.python.org/3/library/inspect.html#types-and-members).
      code = self.load()
    consts = self.load()
    names = self.load()
    varnames = self.load()
    freevars = self.load()
    cellvars = self.load()
    filename = self.load()
    name = self.load()
    firstlineno = self._read_long()
    with self.keep_bytes():
      # lnotab, from
      # https://github.com/python/cpython/blob/master/Objects/lnotab_notes.txt:
      # 'an array of unsigned bytes disguised as a Python bytes object'.
      lnotab = self.load()
    return CodeType(argcount, kwonlyargcount, nlocals, stacksize, flags,
                    code, consts, names, varnames, filename, name, firstlineno,
                    lnotab, freevars, cellvars, self.python_version)

  def load_set(self):
    n = self._read_long()
    args = [self.load() for _ in six.moves.range(n)]
    return set(args)

  def load_frozenset(self):
    n = self._read_long()
    args = [self.load() for _ in six.moves.range(n)]
    return frozenset(args)

  def load_ref(self):
    n = self._read_long()
    return self.refs[n]


def loads(s, python_version):
  um = _LoadCode(s, python_version)
  result = um.load()
  if not um.eof():
    raise BufferError('trailing bytes in marshal data')
  return result



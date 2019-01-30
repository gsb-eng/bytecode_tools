# Copyright (c) 2018 by Srinivas Garlapati

"""Marshal utility.

This implementation is motivated from pypy/lib_pypy/_marshal.py.
"""
import struct
import types

from pydis import compatibility as compat 
from pydis.constants import (
    FLAG_REF as REF, IS_PY2, IS_PY3, MAGIC_NUMBERS, MARSHAL_CODES, PY_VERSION
)

# TODO: Add more version compatibilities.
# Python2 intrepreter should be supported.
class _NULL:
    pass

class CodeType:

    def __init__(
        self,
        argcount,
        kwonlyargcount,
        nlocals,
        stacksize,
        flags,
        code,
        consts,
        names,
        varnames,
        filename,
        name,
        firstlineno,
        lnotab,
        freevars,
        cellvars,
        python_version=PY_VERSION
    ):
        self.co_argcount = argcount
        if python_version >= 3.0:
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


class _Unmarshal:

    def __init__(self):
        self._reflist = []  # Reserve interned objects.
        self._string_reflist = []  # Reserve for loading strings.

    def __call__(self, fp, python_version=None):
        # File pointer opned in binary mode.
        # One should make sure, if the pyc file is passed the first 8/12 bytes
        # should be read before reaching here. otherwise a bad marshal exception
        # occurs.
        self.fp = fp
        self._read = fp.read

        # If no python_version passed, it's the current interpreter version.
        self.python_version = (
            python_version if python_version else PY_VERSION
        )

        return self._load()

    def _read_byte(self, keep_pos=False):
        """Read an unsigned byte.

        Arguments:
            keep_pos: A boolean value to track the current buffer position.
        Returns:
            Single byte value.
        """
        pos = self.fp.tell()
        val = self._read(1)
        if keep_pos:
            self.fp.seek(pos)
        return val

    def _load(self):
        """Load the encodes bytes with marshal.
        """
        c = ord('?')
        try:
            c = ord(self._read_byte())
            if c & REF:
                idx = self._reserve_reflist()
                result = self._load_code_handler(MARSHAL_CODES[c & ~REF])()
                self._reflist[idx] = result
            else:
                result = self._load_code_handler(MARSHAL_CODES[c])()
            return result
        except KeyError:
            raise ValueError('bad marshal code: %r (%02x)' % (chr(c), c))

    def _load_code_handler(self, code):
        """Loading and executing marshal code specific handler.

        Marshal codes are defined in constants.MARSHAL_CODES, each code is
        binded with a specific encoding for serialization purpose.

        Arguments:
            code: Single byte in the byte stream.

        Returns:
            The specifix handlers return type.
        """
        return getattr(self, 'load_{}'.format(code))

    def _reserve_reflist(self):
        index = len(self._reflist)
        self._reflist.append(None)
        return index

    def _mark_ref(self, val):
        self._reflist.append(val)
        return val

    def load_code(self):
        """
        Here is the order of flags loaded on marshal.c

            argcount
            kwonlyargcount
            nlocals
            stacksize
            flags
            code
            consts
            names
            varnames
            freevars
            cellvars
            filename
            name
            firstlineno
            lnotab

            ORDER MATTERS: They are fixed position bytes.
        """
        argcount = self.read_long()
        if self.python_version >= 3.0:
            kwonlyargcount = self.read_long()
        else:
            kwonlyargcount = 0
        nlocals = self.read_long()
        stacksize = self.read_long()
        flags = self.read_long()
        code = self._load()
        consts = self._load()
        names = self._load()
        varnames = self._load()
        freevars = self._load()
        cellvars = self._load()
        filename = self._load()
        name = self._load()
        firstlineno = self.read_long()
        lnotab = self._load()

        return CodeType(
            argcount, kwonlyargcount, nlocals, stacksize, flags,
            code, consts, names, varnames, filename, name, firstlineno,
            lnotab, freevars, cellvars
        )


    def load_null(self):
        return _NULL

    def load_none(self):
        return None

    def load_false(self):
        return False

    def load_true(self):
        return True

    def stopiter(self):
        return StopIteration

    def load_ellipsis(self):
        return Ellipsis

    def r_short(self):
        x = ord(self._read(1)) | (ord(self._read(1)) << 8)
        if x & 0x8000:
            x = x - 0x10000
        return x

    def read_long(self):
        s = self._read(4)
        a = s[0]
        b = s[1]
        c = s[2]
        d = s[3]
        x = a | (b<<8) | (c<<16) | (d<<24)
        if d & 0x80 and x > 0:
            x = -((1 << 32) - x)
            return int(x)
        else:
            return x

    # TODO: handle this with Python2
    # Not required in python3
    def load_int(self):
        if IS_PY3:
            return self.read_long()
        else:
            # TODO: Handle this when it reaches, PY2 interpreters.
            pass

    def load_int64(self):
        # PYTHON'S LONG VALUE BYTE ARRAY IS AS BELOW.....as per longobject.h
        #
        # _PyLong_AsByteArray: Convert the least-significant 8*n bits of long
        # v to a base-256 integer, stored in array bytes.  Normally return 0,
        # return -1 on error.
        # If little_endian is 1/true, store the MSB at bytes[n-1] and the LSB at
        # bytes[0]; else (little_endian is 0/false) store the MSB at bytes[0] and
        # the LSB at bytes[n-1].
        # If is_signed is 0/false, it's an error if v < 0; else (v >= 0) n bytes
        # are filled and there's nothing special about bit 0x80 of the MSB.
        # If is_signed is 1/true, bytes is filled with the 2's-complement
        # representation of v's value.  Bit 0x80 of the MSB is the sign bit.

        b0 = self._read(1)
        b1 = self._read(1)
        b2 = self._read(1)
        b3 = self._read(1)
        b4 = self._read(1)
        b5 = self._read(1)
        b6 = self._read(1)
        b7 = self._read(1)

        # Return this if the value is not signed.
        ret_val = (
            b0 | b1 << 8 | b2 << 16 | b3 << 24 |
            b4 << 32 | b5 << 40 | b6 << 48 | b7 << 56
        )
        # Handle signed case.
        if b7 & 0x80:
            ret_val = -((1 << 64) - ret_val)

        return ret_val

    def load_float(self):
        size = self._read(1)
        return float(self._read(int(size)))

    def load_binary_float(self):
        return struct.unpack('<d', self._read(8))[0]

    def load_long(self):
        # It lands here if the numeric value is >= 64 bit

        # Python can handle values bigger to fit in 64 bit, but that needs to be
        # handled logically.
        # In PYC context, if the number goes beyond signed 64 bit range, it gets
        # converted into multiple 16 bit numbers.
        #
        # Statement from marshal.c
        #
        # We assume that Python ints are stored internally in base some power of
        # 2**15; for the sake of portability we'll always read and write them
        # in base exactly 2**15.
        #
        # Certainly this is because, the INT in python is signed and it ranges
        # from -32768 to 32767 -->. -2**15 to 2**15 - 1. So this would help
        # poratbility to python native int.
        #
        # I.e: n = 14273427342342384723428347234
        #
        # d = (n & (2**15 - 1)) -> 3426
        #   n >>= 15 --> 435590434031444846296031
        # d = (n & (2**15 - 1)) -> 15327
        #   n >>= 15 --> 13293165101057276803
        # d = (n & (2**15 - 1)) -> 31619
        #   n >>= 15 --> 405675204500038
        # d = (n & (2**15 - 1)) -> 23110
        #   n >>= 15 --> 12380224746
        # d = (n & (2**15 - 1)) -> 15594
        #   n >>= 15 --> 377814
        # d = (n & (2**15 - 1)) -> 17366
        #   n >>= 15 --> 11
        # d = (n & (2**15 - 1)) -> 11
        #   n >>= 15 --> 0

        # Hence the digit size here is 7 and the digits are, as below.
        #     digits = [3426, 15327, 31619, 23110, 15594, 17366, 11]

        # To get the actual number back.
        # final_val = 0
        # for val in [0, 1, 2, 3, 4, 5, 6] --> total 7
        #     final_val |= digits[0] << val *15
        #
        # If we decode the above loop
        # final_val = 0
        # 0: final_val |= 3426 << (0 * 15) --> 3426
        # 1: final_val |= 15327 << (1 * 15) --> 502238562
        # 2: final_val |= 31619 << (2 * 15) --> 33951144971618
        # 3: final_val |= 23110 << (3 * 15) --> 813144790117879138
        # 4: final_val |= 15594 << (4 * 15) --> 17979471087629289622882
        # 5: final_val |= 17366 << (5 * 15) --> 656086910203201699537980770
        # 6: final_val |= 11 << (6 * 15) --> 14273427342342384723428347234
        #
        # Negative values are as simple as positive, just the sign gets stored
        # along with number of digits.
        digit_size = self.read_long()
        sign = -1 if digit_size < 0 else 1
        x = 0
        for i in range(digit_size):
            d = self.r_short()
            x = x | (d<<(i*15))
        return x * sign

    def load_string(self):
        size = self.read_long()
        val = self._read(size)

        if IS_PY3:
            return compat.BytesType(val)
        else:
            # Handle Python2 case, the current interpreter is of python3 and
            # handling Python2 generated PYC file. then convert bytes to native
            # str
            pass

    def load_interned(self):
        # Interned objects are stored as 4*octa --> 32 bits.
        size = self.read_long()
        val = self._read(size)
        self._string_reflist.append(val)
        return self._mark_ref(val)

    def load_stringref(self):
        index = self.read_long()
        return self._string_reflist[index]

    def load_list(self):
        size = self.read_long()
        ret_val = [self._load() for i in range(size)]
        return ret_val

    def load_tuple(self):
        return tuple(self.load_list())

    def load_small_tuple(self):
        size = ord(self._read_byte())
        ret_val = [self._load() for i in range(size)]
        return tuple(ret_val)

    def load_set(self):
        return set(self.load_list())

    def load_frozenset(self):
        return frozenset(self.load_list())

    def load_dict(self):
        temp_dict = {}

        while 1:
            key = self._load()
            if key == None:
                break
            value = self._load()
            temp_dict[key] = value
        return temp_dict

    def load_unicode(self):
        size = self.read_long()
        unicode_bytes = self._read(size)

        # TODO: Handle version incompatibilities with unicode.
        return unicode_bytes.decode('utf-8')

    def load_ref(self):
        index = self.read_long()
        return self._reflist[index]

    def load_ascii(self):
        size = self.read_long()
        return compat.native_str(self._read(size))

    def load_ascii_interned(self):
        size = self._read_byte()
        interned_ascii = compat.native_str(self._read(size))
        self._string_reflist.append(interned_ascii)
        return interned_ascii

    def load_short_ascii(self):
        size = ord(self._read_byte())
        return compat.native_str(self._read(size))

    def load_short_ascii_interned(self):
        size = ord(self._read_byte())
        interned = compat.native_str(self._read(size))
        self._string_reflist.append(interned)
        return interned


load = _Unmarshal()
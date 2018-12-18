# Copyright (c) 2018 by Srinivas Garlapati

"""Marshal utility.
"""
import struct

from pydis import compatibility as compat 
from pydis.constants import (
    FLAG_REF as REF, IS_PY2, IS_PY3, MAGIC_NUMBERS, MARSHAL_CODES, PY_VERSION
)

# TODO: Add more version compatibilities.
# Python2 intrepreter should be supported.
class _NULL:
    pass


class _Unmarshal:

    def __init__(self, fp, python_version):
        self._read = fp
        self.python_version = python_version

    def _load_code_handler(self, code):
        """Loading and executing marshal code specific handler.

        Marshal codes are defined in constants.MARSHAL_CODES, each code is
        binded with a specific encoding for serialization purpose.

        Arguments:
            code: Single byte in the byte stream.

        Returns:
            The specifix handlers return type.
        """
        return getattr(self, 'load_{}'.format(code))()

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

    def r_long(self):
        s = self._read(4)
        a = ord(s[0])
        b = ord(s[1])
        c = ord(s[2])
        d = ord(s[3])
        x = a | (b<<8) | (c<<16) | (d<<24)
        if d & 0x80 and x > 0:
            x = -((1 << 32) - x)
            return int(x)
        else:
            return x

    # TODO: handle this with Python2
    # Not required in python3
    def load_int(self):
        pass

    def load_int64(self):
        pass

    def load_float(self):
        pass

    def load_binary_float(self):
        pass

    def load_long(self):
        size = self.r_long()
        sign = 1
        if size < 0:
            sign = -1
            size = -size
        x = 0
        for i in range(size):
            d = self.r_short()
            x = x | (d<<(i*15))
        return x * sign

    def load_string(self):
        pass

    def load_interned(self):
        pass

    def stringref(self):
        pass

    def load_tuple(self):
        pass

    def load_list(self):
        pass

    def load_dict(self):
        pass

    def load_code(self):
        pass

    def load_unicode(self):
        pass

    def load_unknown(self):
        pass

    def load_set(self):
        pass

    def load_frozenset(self):
        pass

    def load_ref(self):
        pass

    def load_ascii(self):
        pass

    def load_ascii_interned(self):
        pass

    def load_tuple(self):
        pass

    def load_short_ascii(self):
        pass

    def load_short_ascii_interned(self):
        pass
# Copyright (c) 2018 by Srinivas Garlapati

"""Marshal utility.
"""
import struct

from pydis import compatibility as compat 
from pydis.constants import FLAG_REF as REF, MARSHAL_CODES
from pydis.constants import IS_PY2, IS_PY3, MAGIC_NUMBERS, PY_VERSION


# TODO: Add more version compatibilities.
# Python2 intrepreter should be supported.


class _Unmarshal:

    def __init__(self, fp, python_version):
        self.fp. =fp
        self.python_version = python_version


    def load_null(self):
        return None

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

    def load_int(self):
        pass

    def load_int64(self):
        pass

    def load_float(self):
        pass

    def load_binary_float(self):
        pass

    def load_long(self):
        pass

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
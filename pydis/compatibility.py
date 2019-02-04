# Copyright (c) 2018 by Srinivas Garlapati

"""Python version compatibility functions."""

import sys

from pydis.constants import IS_PY3


def native_str(s):
  """Convert a bytes or unicode object to the native str type."""
  if isinstance(s, str):
    return s
  elif sys.version_info[0] < 3:
    return s.encode("utf-8")
  else:
    return s.decode("utf-8")


if IS_PY3:
    BytesType = bytes
    UnicodeType = str
    LongType = int
else:
    BytesType = bytes
    UnicodeType = unicode
    LongType = long
"""Python version numbers."""

import struct

from pydis.constants import IS_PY3, MAGIC_NUMBERS


def decode_magic_to_version(magic):
    """To get the magic number from the encoded word.

    Magic number is a 16 bit unsigned little endian encoded byte string in the
    pyc files, this will be used to invalidate bytecode between incompatible
    bytecode versions.

    Arguments:
      magic: A 16 bit unsigned little endian encoded byte string

    Returns:
      Python ver
    """
    return MAGIC_NUMBERS[struct.unpack('<H', magic)]


def decode_header(header_bytes):
    """Returns the decoded header part of pyc file.

    pyc file structure varied from 2.x to 3.x or even between 3.x versions.
    """
    pass

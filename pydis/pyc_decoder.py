# Copyright (c) 2018 by Srinivas Garlapati

"""Module to deal with loading pyc files data."""

import datetime
import io
import mimetypes
import os
import struct

from pydis.constants import (
    IS_PY3, MAGIC_NUMBERS, PYC_MIME_TYPE, V3, V4
)
from pydis.unmarshal import load


class UnknowMagic(Exception):
    pass


def __read_unsigned_int(fp):
    return struct.unpack('I', fp.read(4))[0]


def magic_to_version(magic):
    """To get the magic number from the encoded word.

    Magic number is a 16 bit unsigned little endian encoded byte string in the
    pyc files, this will be used to invalidate bytecode between incompatible
    bytecode versions.

    Arguments:
      magic: A 16 bit unsigned little endian encoded byte string

    Returns:
p    """
    return MAGIC_NUMBERS[struct.unpack('<H', magic)]


def _decode_magic(fp):
    """Function to decode magic number of given pyc file.

    First four bytes are reserved for magic number, in 4 only the first 2 bytes
    actually holds the magic number and the remaingin 2 bytes are '\\r\\n', they
    are used to invalidate if the file is open in text mode instead binary mode.
    """
    return struct.unpack('Hcc', fp.read(4))[0]


def _decode_timestamp_bytes(fp, magic):
    """Timestamp bytes varies from V3 to V4 in Py3, till magic 3393, it's 12
    bytes header, but later added a extra 4 bytes to include hash based
    validation of pyc's, refer PEP 552 for more info on this.
    """
    if MAGIC_NUMBERS[magic][1] == V4:
        determ_bits = __read_unsigned_int(fp)
        if not determ_bits:
            ts = __read_unsigned_int(fp)
            ts = datetime.datetime.utcfromtimestamp(ts).strftime(
                '%Y-%m-%d %H:%M:%S'
            )
        else:
            ts = __read_unsigned_int(fp)
    else:
        ts = __read_unsigned_int(fp)
        ts = datetime.datetime.utcfromtimestamp(ts).strftime(
            '%Y-%m-%d %H:%M:%S'
        )
    return ts


def _decode_size_bytes(fp):
    """Last 4 bytes in pyc header represents the size of code object.

    TODO: This is not supported in 2.x, make sure it is fixed while handling
      2.x versions.
    """
    return __read_unsigned_int(fp)


def _decode_header(fp):
    """Returns the decoded header part of pyc file.

    pyc file structure varied from 2.x to 3.x or even between 3.x versions. At
    this point pydis only supporting 3.x versions. We see there is a change
    happened at 3393 ==> 3.7b1 version.
    """
    magic = _decode_magic(fp)
    if magic not in MAGIC_NUMBERS:
        raise unknownMagic('Magic number is not valid.')
    ts = _decode_timestamp_bytes(fp, magic)
    size = _decode_size_bytes(fp)
    return magic, ts, size


def decode_pyc(file_or_bytes):
    """Decoding the pyc files, this will accept a pyc file or a bytes array and
    even the io.BytesIo buffer.

    Arguments:
        file_or_bytes: A path path as a string or bytes array/ BytesIo object.

    Returns: A tuple having below objects...
        magic: magic number found in the pyc.
        ts:  Timestamp found in the pyc.
        size: size of the source found in the pyc.
        Code object retrieved from the buffer/given pyc file.
    """
    if isinstance(file_or_bytes, str) and os.path.exists(file_or_bytes):
        # PYC file mime type should be of `application/x-python-code`
        assert mimetypes.guess_type(file_or_bytes)[0] == PYC_MIME_TYPE
        fp = open(file_or_bytes, 'rb')
    elif isinstance(file_or_bytes, bytes):
        fp = io.BytesIO(file_or_bytes)
    elif isinstance(file_or_bytes, io.BytesIO):
        fp = file_or_bytes
    else:
        raise ValueError('No resource found with %s' % file_or_bytes)

    magic, ts, size = _decode_header(fp)
    code_object = load(fp, python_version=MAGIC_NUMBERS[magic][0])
    fp.close()

    return magic, ts, size, code_object

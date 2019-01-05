# Copyright (c) 2018 by Srinivas Garlapati

"""
All the constants that needs to be loaded for usage at different levels. 
"""

import sys


FLAG_REF = 0x80

PY_VERSION_STR = '{}.{}'.format(sys.version_info[0], sys.version_info[1])
PY_VERSION = float(PY_VERSION_STR)

IS_PY2 = True if PY_VERSION >= 2 and PY_VERSION < 3 else False
IS_PY3 = True if PY_VERSION >= 3 else False

PYC_MIME_TYPE = 'application/x-python-code'
# Python bytecode files stores a magic number to invalidate version
# incomatibalities, it's a 2 byte unsigned integer in little endian encoded.
# These constants are taken from -
#   Python source code: Lib/importlib/_bootstrap_external.py

V1 = 8
V2 = 12
V3 = 12
V4 = 16

MAGIC_NUMBERS = {
    # Python 1
    20121: ((1, 5), V1),
    50428: ((1, 6), V1),

    # Python 2
    50823: ((2, 0), V1),
    60202: ((2, 1), V3),
    60717: ((2, 2), V3),
    62011: ((2, 3), V3),  # a0
    62021: ((2, 3), V3),  # a0
    62041: ((2, 4), V3),  # a0
    62051: ((2, 4), V3),  # a3
    62061: ((2, 4), V3),  # b1
    62071: ((2, 5), V3),  # a0
    62081: ((2, 5), V3),  # a0
    62091: ((2, 5), V3),  # a0
    62092: ((2, 5), V3),  # a0
    62101: ((2, 5), V3),  # b3
    62111: ((2, 5), V3),  # b3
    62121: ((2, 5), V3),  # c1
    62131: ((2, 5), V3),  # c2
    62151: ((2, 6), V3),  # a0
    62161: ((2, 6), V3),  # a1
    62171: ((2, 7), V3),  # a0
    62181: ((2, 7), V3),  # a0
    62191: ((2, 7), V3),  # a0
    62201: ((2, 7), V3),  # a0
    62211: ((2, 7), V3),  # a0

    # Python 3
    3000: ((3, 0), V3),
    3010: ((3, 0), V3),
    3020: ((3, 0), V3),
    3030: ((3, 0), V3),
    3040: ((3, 0), V3),
    3050: ((3, 0), V3),
    3060: ((3, 0), V3),
    3061: ((3, 0), V3),
    3071: ((3, 0), V3),
    3081: ((3, 0), V3),
    3091: ((3, 0), V3),
    3101: ((3, 0), V3),
    3103: ((3, 0), V3),
    3111: ((3, 0), V3),  # a4
    3131: ((3, 0), V3),  # a5

    # Python 3.1
    3141: ((3, 1), V3),  # a0
    3151: ((3, 1), V3),  # a0

    # Python 3.2
    3160: ((3, 2), V3),  # a0
    3170: ((3, 2), V3),  # a1
    3180: ((3, 2), V3),  # a2

    # Python 3.3
    3190: ((3, 3), V3),  # a0
    3200: ((3, 3), V3),  # a0
    3220: ((3, 3), V3),  # a1
    3230: ((3, 3), V3),  # a4

    # Python 3.4
    3250: ((3, 4), V3),  # a1
    3260: ((3, 4), V3),  # a1
    3270: ((3, 4), V3),  # a1
    3280: ((3, 4), V3),  # a1
    3290: ((3, 4), V3),  # a4
    3300: ((3, 4), V3),  # a4
    3310: ((3, 4), V3),  # rc2

    # Python 3.5
    3320: ((3, 5), V3),  # a0
    3330: ((3, 5), V3),  # b1
    3340: ((3, 5), V3),  # b2
    3350: ((3, 5), V3),  # b2
    3351: ((3, 5), V3),  # 3.5.2

    # Python 3.6
    3360: ((3, 6), V3),  # a0
    3361: ((3, 6), V3),  # a0
    3370: ((3, 6), V3),  # a1
    3371: ((3, 6), V3),  # a1
    3372: ((3, 6), V3),  # a1
    3373: ((3, 6), V3),  # b1
    3375: ((3, 6), V3),  # b1
    3376: ((3, 6), V3),  # b1
    3377: ((3, 6), V3),  # b1
    3378: ((3, 6), V3),  # b2
    3379: ((3, 6), V3),  # rc1

    # Python 3.7
    3390: ((3, 7), V3),  # a1
    3391: ((3, 7), V3),  # a2
    3392: ((3, 7), V3),  # a4
    3393: ((3, 7), V4),  # b1
    3394: ((3, 7), V4),  # b5
}

MARSHAL_CODES_HEX = {
    0x30: 'null',
    0x4e: 'none',
    0x46: 'false',
    0x54: 'true',
    0x53: 'stopiter',
    0x2e: 'ellipsis',
    0x69: 'int',
    0x49: 'int64',
    0x66: 'float',
    0x67: 'binary_float',
    0x78: 'complex',
    0x79: 'binary_complex',
    0x6c: 'long',
    0x73: 'string',
    0x74: 'interned',
    0x52: 'stringref',
    0x28: 'tuple',
    0x5b: 'list',
    0x7b: 'dict',
    0x63: 'code',
    0x75: 'unicode',
    0x3f: 'unknown',
    0x3c: 'set',
    0x3e: 'frozenset',
    0x72: 'ref',
    0x61: 'ascii',
    0x41: 'ascii_interned',
    0x29: 'small_tuple',
    0x7a: 'short_ascii',
    0x5a: 'short_ascii_interned'
}

MARSHAL_CODES = {
    48: 'none',
    78: 'none',
    70: 'false',
    84: 'true',
    83: 'stopiter',
    46: 'ellipsis',
    105: 'int',
    73: 'int64',
    102: 'float',
    103: 'binary_float',
    120: 'complex',
    121: 'binary_complex',
    108: 'long',
    115: 'string',
    116: 'interned',
    82: 'stringref',
    40: 'tuple',
    91: 'list',
    123: 'dict',
    99: 'code',
    117: 'unicode',
    63: 'unknown',
    60: 'set',
    62: 'frozenset',
    114: 'ref',
    97: 'ascii',
    65: 'ascii_interned',
    41: 'small_tuple',
    122: 'short_ascii',
    90: 'short_ascii_interned'
}
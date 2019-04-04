# Copyright (c) 2018 by Srinivas Garlapati

"""
All the constants that needs to be loaded for usage at different levels. 
"""

import sys


FLAG_REF = 0x80

PY_VERSION_STR = '{majr}.{minr}'.format(
    majr=sys.version_info[0], minr=sys.version_info[1]
)
PY_VERSION = float(PY_VERSION_STR)

IS_PY2 = True if PY_VERSION >= 2 and PY_VERSION < 3 else False
IS_PY3 = True if PY_VERSION >= 3 else False

PYC_MIME_TYPE = 'application/x-python-code'
# Python bytecode files stores a magic number to invalidate version
# incomatibalities, it's a 2 byte unsigned integer in little endian encoded.
# These constants are taken from -
#   Python source code: Lib/importlib/_bootstrap_external.py

V1 = 8
V2 = 8
V3 = 12
V4 = 16

MAGIC_NUMBERS = {
    # Python 1
    20121: (1.5, V1),
    50428: (1.6, V1),

    # Python 2
    50823: (2.0, V1),
    60202: (2.1, V2),
    60717: (2.2, V2),
    62011: (2.3, V2),  # a0
    62021: (2.3, V2),  # a0
    62041: (2.4, V2),  # a0
    62051: (2.4, V2),  # a3
    62061: (2.4, V2),  # b1
    62071: (2.5, V2),  # a0
    62081: (2.5, V2),  # a0
    62091: (2.5, V2),  # a0
    62092: (2.5, V2),  # a0
    62101: (2.5, V2),  # b3
    62111: (2.5, V2),  # b3
    62121: (2.5, V2),  # c1
    62131: (2.5, V2),  # c2
    62151: (2.6, V2),  # a0
    62161: (2.6, V2),  # a1
    62171: (2.7, V2),  # a0
    62181: (2.7, V2),  # a0
    62191: (2.7, V2),  # a0
    62201: (2.7, V2),  # a0
    62211: (2.7, V2),  # a0

    # Python 3
    3000: (3.0, V3),
    3010: (3.0, V3),
    3020: (3.0, V3),
    3030: (3.0, V3),
    3040: (3.0, V3),
    3050: (3.0, V3),
    3060: (3.0, V3),
    3061: (3.0, V3),
    3071: (3.0, V3),
    3081: (3.0, V3),
    3091: (3.0, V3),
    3101: (3.0, V3),
    3103: (3.0, V3),
    3111: (3.0, V3),  # a4
    3131: (3.0, V3),  # a5

    # Python 3.1
    3141: (3.1, V3),  # a0
    3151: (3.1, V3),  # a0

    # Python 3.2
    3160: (3.2, V3),  # a0
    3170: (3.2, V3),  # a1
    3180: (3.2, V3),  # a2

    # Python 3.3
    3190: (3.3, V3),  # a0
    3200: (3.3, V3),  # a0
    3220: (3.3, V3),  # a1
    3230: (3.3, V3),  # a4

    # Python 3.4
    3250: (3.4, V3),  # a1
    3260: (3.4, V3),  # a1
    3270: (3.4, V3),  # a1
    3280: (3.4, V3),  # a1
    3290: (3.4, V3),  # a4
    3300: (3.4, V3),  # a4
    3310: (3.4, V3),  # rc2

    # Python 3.5
    3320: (3.5, V3),  # a0
    3330: (3.5, V3),  # b1
    3340: (3.5, V3),  # b2
    3350: (3.5, V3),  # b2
    3351: (3.5, V3),  # 3.5.2

    # Python 3.6
    3360: (3.6, V3),  # a0
    3361: (3.6, V3),  # a0
    3370: (3.6, V3),  # a1
    3371: (3.6, V3),  # a1
    3372: (3.6, V3),  # a1
    3373: (3.6, V3),  # b1
    3375: (3.6, V3),  # b1
    3376: (3.6, V3),  # b1
    3377: (3.6, V3),  # b1
    3378: (3.6, V3),  # b2
    3379: (3.6, V3),  # rc1

    # Python 3.7
    3390: (3.7, V3),  # a1
    3391: (3.7, V3),  # a2
    3392: (3.7, V3),  # a4
    3393: (3.7, V4),  # b1
    3394: (3.7, V4),  # b5
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
    0: 'none',
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

HAS_CONST = 1
HAS_NAME = 2
HAS_JREL = 4
HAS_JABS = 8
HAS_LOCAL = 16
HAS_CMP = 32
HAS_FREE = 64
HAS_ARG = 128
HAS_NARGS = 256
IS_EXTENDED_ARG = 512
IS_MAKE_FUNCTION = 1024
IS_FORMAT_VALUE = 2048

CMP_OP = (
    '<', '<=', '==', '!=', '>', '>=', 'in', 'not in', 'is',
    'is not', 'exception match', 'BAD'
)

OPCODES_3 = {
    1: ('POP_TOP', 0),
    2: ('ROT_TWO', 0),
    3: ('ROT_THREE', 0),
    4: ('DUP_TOP', 0),
    5: ('DUP_TOP_TWO', 0),
    9: ('NOP', 0),
    10: ('UNARY_POSITIVE', 0),
    11: ('UNARY_NEGATIVE', 0),
    12: ('UNARY_NOT', 0),
    15: ('UNARY_INVERT', 0),
    16: ('BINARY_MATRIX_MULTIPLY', 0),
    17: ('INPLACE_MATRIX_MULTIPLY', 0),
    19: ('BINARY_POWER', 0),
    20: ('BINARY_MULTIPLY', 0),
    22: ('BINARY_MODULO', 0),
    23: ('BINARY_ADD', 0),
    24: ('BINARY_SUBTRACT', 0),
    25: ('BINARY_SUBSCR', 0),
    26: ('BINARY_FLOOR_DIVIDE', 0),
    27: ('BINARY_TRUE_DIVIDE', 0),
    28: ('INPLACE_FLOOR_DIVIDE', 0),
    29: ('INPLACE_TRUE_DIVIDE', 0),
    50: ('GET_AITER', 0),
    51: ('GET_ANEXT', 0),
    52: ('BEFORE_ASYNC_WITH', 0),
    54: ('STORE_MAP', 0),
    55: ('INPLACE_ADD', 0),
    56: ('INPLACE_SUBTRACT', 0),
    57: ('INPLACE_MULTIPLY', 0),
    59: ('INPLACE_MODULO', 0),
    60: ('STORE_SUBSCR', 0),
    61: ('DELETE_SUBSCR', 0),
    62: ('BINARY_LSHIFT', 0),
    63: ('BINARY_RSHIFT', 0),
    64: ('BINARY_AND', 0),
    65: ('BINARY_XOR', 0),
    66: ('BINARY_OR', 0),
    67: ('INPLACE_POWER', 0),
    68: ('GET_ITER', 0),
    69: ('STORE_LOCALS', 0),
    70: ('PRINT_EXPR', 0),
    71: ('LOAD_BUILD_CLASS', 0),
    72: ('YIELD_FROM', 0),
    73: ('GET_AWAITABLE', 0),
    75: ('INPLACE_LSHIFT', 0),
    76: ('INPLACE_RSHIFT', 0),
    77: ('INPLACE_AND', 0),
    78: ('INPLACE_XOR', 0),
    79: ('INPLACE_OR', 0),
    80: ('BREAK_LOOP', 0),
    81: ('WITH_CLEANUP', 0),
    82: ('WITH_CLEANUP_FINISH', 0),
    83: ('RETURN_VALUE', 0),
    84: ('IMPORT_STAR', 0),
    86: ('YIELD_VALUE', 0),
    87: ('POP_BLOCK', 0),
    88: ('END_FINALLY', 0),
    89: ('POP_EXCEPT', 0),
    90: ('STORE_NAME', 130),
    91: ('DELETE_NAME', 130),
    92: ('UNPACK_SEQUENCE', 128),
    93: ('FOR_ITER', 132),
    94: ('UNPACK_EX', 128),
    95: ('STORE_ATTR', 130),
    96: ('DELETE_ATTR', 130),
    97: ('STORE_GLOBAL', 130),
    98: ('DELETE_GLOBAL', 130),
    100: ('LOAD_CONST', 129),
    101: ('LOAD_NAME', 130),
    102: ('BUILD_TUPLE', 128),
    103: ('BUILD_LIST', 128),
    104: ('BUILD_SET', 128),
    105: ('BUILD_MAP', 128),
    106: ('LOAD_ATTR', 130),
    107: ('COMPARE_OP', 160),
    108: ('IMPORT_NAME', 130),
    109: ('IMPORT_FROM', 130),
    110: ('JUMP_FORWARD', 132),
    111: ('JUMP_IF_FALSE_OR_POP', 136),
    112: ('JUMP_IF_TRUE_OR_POP', 136),
    113: ('JUMP_ABSOLUTE', 136),
    114: ('POP_JUMP_IF_FALSE', 136),
    115: ('POP_JUMP_IF_TRUE', 136),
    116: ('LOAD_GLOBAL', 130),
    119: ('CONTINUE_LOOP', 128),
    120: ('SETUP_LOOP', 132),
    121: ('SETUP_EXCEPT', 132),
    122: ('SETUP_FINALLY', 132),
    124: ('LOAD_FAST', 144),
    125: ('STORE_FAST', 144),
    126: ('DELETE_FAST', 144),
    130: ('RAISE_VARARGS', 128),
    131: ('CALL_FUNCTION', 128),
    132: ('MAKE_FUNCTION', 128),
    133: ('BUILD_SLICE', 128),
    134: ('MAKE_CLOSURE', 128),
    135: ('LOAD_CLOSURE', 192),
    136: ('LOAD_DEREF', 192),
    137: ('STORE_DEREF', 192),
    138: ('DELETE_DEREF', 192),
    140: ('CALL_FUNCTION_VAR', 128),
    141: ('CALL_FUNCTION_KW', 128),
    142: ('CALL_FUNCTION_VAR_KW', 128),
    143: ('SETUP_WITH', 132),
    144: ('EXTENDED_ARG', 640),
    145: ('LIST_APPEND', 128),
    146: ('SET_ADD', 128),
    147: ('MAP_ADD', 128),
    148: ('LOAD_CLASSDEREF', 192),
    149: ('BUILD_LIST_UNPACK', 128),
    150: ('BUILD_MAP_UNPACK', 128),
    151: ('BUILD_MAP_UNPACK_WITH_CALL', 128),
    152: ('BUILD_TUPLE_UNPACK', 128),
    153: ('BUILD_SET_UNPACK', 128),
    154: ('SETUP_ASYNC_WITH', 132),
    160: ('LOAD_METHOD', 130),
    161: ('CALL_METHOD', 128),
}

# Taken Python-2.5 as base here.
OPCODES_2 = {
    0: ('STOP_CODE', 0),
    1: ('POP_TOP', 0),
    2: ('ROT_TWO', 0),
    3: ('ROT_THREE', 0),
    4: ('DUP_TOP', 0),
    5: ('ROT_FOUR', 0),
    9: ('NOP', 0),
    10: ('UNARY_POSITIVE', 0),
    11: ('UNARY_NEGATIVE', 0),
    12: ('UNARY_NOT', 0),
    13: ('UNARY_CONVERT', 0),
    15: ('UNARY_INVERT', 0),
    18: ('LIST_APPEND', 0),
    19: ('BINARY_POWER', 0),
    20: ('BINARY_MULTIPLY', 0),
    21: ('BINARY_DIVIDE', 0),
    22: ('BINARY_MODULO', 0),
    23: ('BINARY_ADD', 0),
    24: ('BINARY_SUBTRACT', 0),
    25: ('BINARY_SUBSCR', 0),
    26: ('BINARY_FLOOR_DIVIDE', 0),
    27: ('BINARY_TRUE_DIVIDE', 0),
    28: ('INPLACE_FLOOR_DIVIDE', 0),
    29: ('INPLACE_TRUE_DIVIDE', 0),
    30: ('SLICE+0', 0),
    31: ('SLICE+1', 0),
    32: ('SLICE+2', 0),
    33: ('SLICE+3', 0),
    40: ('STORE_SLICE+0', 0),
    41: ('STORE_SLICE+1', 0),
    42: ('STORE_SLICE+2', 0),
    43: ('STORE_SLICE+3', 0),
    50: ('DELETE_SLICE+0', 0),
    51: ('DELETE_SLICE+1', 0),
    52: ('DELETE_SLICE+2', 0),
    53: ('DELETE_SLICE+3', 0),
    55: ('INPLACE_ADD', 0),
    56: ('INPLACE_SUBTRACT', 0),
    57: ('INPLACE_MULTIPLY', 0),
    58: ('INPLACE_DIVIDE', 0),
    59: ('INPLACE_MODULO', 0),
    60: ('STORE_SUBSCR', 0),
    61: ('DELETE_SUBSCR', 0),
    62: ('BINARY_LSHIFT', 0),
    63: ('BINARY_RSHIFT', 0),
    64: ('BINARY_AND', 0),
    65: ('BINARY_XOR', 0),
    66: ('BINARY_OR', 0),
    67: ('INPLACE_POWER', 0),
    68: ('GET_ITER', 0),
    70: ('PRINT_EXPR', 0),
    71: ('PRINT_ITEM', 0),
    72: ('PRINT_NEWLINE', 0),
    73: ('PRINT_ITEM_TO', 0),
    74: ('PRINT_NEWLINE_TO', 0),
    75: ('INPLACE_LSHIFT', 0),
    76: ('INPLACE_RSHIFT', 0),
    77: ('INPLACE_AND', 0),
    78: ('INPLACE_XOR', 0),
    79: ('INPLACE_OR', 0),
    80: ('BREAK_LOOP', 0),
    81: ('WITH_CLEANUP', 0),
    82: ('LOAD_LOCALS', 0),
    83: ('RETURN_VALUE', 0),
    84: ('IMPORT_STAR', 0),
    85: ('EXEC_STMT', 0),
    86: ('YIELD_VALUE', 0),
    87: ('POP_BLOCK', 0),
    88: ('END_FINALLY', 0),
    89: ('BUILD_CLASS', 0),
    90: ('STORE_NAME', 130),
    91: ('DELETE_NAME', 130),
    92: ('UNPACK_SEQUENCE', 128),
    93: ('FOR_ITER', 132),
    95: ('STORE_ATTR', 130),
    96: ('DELETE_ATTR', 130),
    97: ('STORE_GLOBAL', 130),
    98: ('DELETE_GLOBAL', 130),
    99: ('DUP_TOPX', 128),
    100: ('LOAD_CONST', 129),
    101: ('LOAD_NAME', 130),
    102: ('BUILD_TUPLE', 128),
    103: ('BUILD_LIST', 128),
    104: ('BUILD_MAP', 128),
    105: ('LOAD_ATTR', 130),
    106: ('COMPARE_OP', 160),
    107: ('IMPORT_NAME', 130),
    108: ('IMPORT_FROM', 130),
    110: ('JUMP_FORWARD', 132),
    111: ('JUMP_IF_FALSE', 132),
    112: ('JUMP_IF_TRUE', 132),
    113: ('JUMP_ABSOLUTE', 136),
    116: ('LOAD_GLOBAL', 130),
    119: ('CONTINUE_LOOP', 136),
    120: ('SETUP_LOOP', 132),
    121: ('SETUP_EXCEPT', 132),
    122: ('SETUP_FINALLY', 132),
    124: ('LOAD_FAST', 144),
    125: ('STORE_FAST', 144),
    126: ('DELETE_FAST', 144),
    130: ('RAISE_VARARGS', 128),
    131: ('CALL_FUNCTION', 128),
    132: ('MAKE_FUNCTION', 128),
    133: ('BUILD_SLICE', 128),
    134: ('MAKE_CLOSURE', 128),
    135: ('LOAD_CLOSURE', 192),
    136: ('LOAD_DEREF', 192),
    137: ('STORE_DEREF', 192),
    140: ('CALL_FUNCTION_VAR', 128),
    141: ('CALL_FUNCTION_KW', 128),
    142: ('CALL_FUNCTION_VAR_KW', 128),
    143: ('EXTENDED_ARG', 640)
}
OPCODES_2_5 = OPCODES_2.copy()

OPCODES_2_6 = OPCODES_2.copy()
OPCODES_2_6.update({
    54: ('STORE_MAP', 0)
})

OPCODES_2_7 = OPCODES_2_6.copy()
OPCODES_2_7.update({
    94: ('LIST_APPEND', 128),
    104: ('BUILD_SET', 128),
    105: ('BUILD_MAP', 128),
    106: ('LOAD_ATTR', 130),
    107: ('COMPARE_OP', 160),
    108: ('IMPORT_NAME', 130),
    109: ('IMPORT_FROM', 130),
    111: ('JUMP_IF_FALSE_OR_POP', 136),
    112: ('JUMP_IF_TRUE_OR_POP', 136),
    114: ('POP_JUMP_IF_FALSE', 136),
    115: ('POP_JUMP_IF_TRUE', 136),
    143: ('SETUP_WITH', 132),
    145: ('EXTENDED_ARG', 640),
    146: ('SET_ADD', 128),
    147: ('MAP_ADD', 128)

})

OPCODES_2_7.pop(18)  # LIST_APPND has been changed to 94 from 18


OPCODES_3_0 = OPCODES_3.copy()

OPCODES_3_1 = OPCODES_3.copy()

OPCODES_3_2 = OPCODES_3.copy()

OPCODES_3_3 = OPCODES_3.copy()

OPCODES_3_4 = OPCODES_3.copy()

OPCODES_3_5 = OPCODES_3.copy()

# overrrided opcdes in 3.5
OPCODES_3_5.update({
    69: ('GET_YIELD_FROM_ITER', 0),
    81: ('WITH_CLEANUP_START', 0),
})

# Removed opcodes in 3.5
OPCODES_3_5.pop(54)

OPCODES_3_6 = OPCODES_3_5.copy()
OPCODES_3_6.update({
    85: ('SETUP_ANNOTATIONS', 128),
    127: ('STORE_ANNOTATION', 128),
    142: ('CALL_FUNCTION_EX', 128),
    155: ('FORMAT_VALUE', 128),
    156: ('BUILD_CONST_KEY_MAP', 128),
    157: ('BUILD_STRING', 128),
    158: ('BUILD_TUPLE_UNPACK_WITH_CALL', 128)
})

# Removed opcodes in 3.6
OPCODES_3_6.pop(140)

OPCODES_3_7 = OPCODES_3_6.copy()
OPCODES_3_7.update({
    160: ('LOAD_METHOD', 128),
    161: ('CALL_METHOD', 128)
})

HAS_ARGUMENT = 90  # Opcode > 90 have arguments to deal with

# Opcodes with name table lookup required.
NAME_OPCODES = (
    90, 91, 95, 96, 97, 98, 101, 106, 108, 109, 116, 160
)

# Opcodes with relative jump.
JREL_OPCODES = (93, 110, 120, 122, 143, 154, 162)

# Opcodes with absolute jump.
JABS_OPCODES = (111, 112, 113, 114, 115, 121)

# Opcodes with constants.
CONST_OPCODES = (100,)

# Opcodes with compare operator.
CMP_OPCODES = (107,)

# Opcodes with local variables involved.
LOCAL_OPCODES = (124, 125, 126)

# Opcodes with free variables involved, like closure.
FREE_OPCODES = (135, 136, 137, 138, 148)

NARGS_OPCODES = (None, )

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

HAS_CONST = 1
HAS_NAME = 2
HAS_JREL = 4
HAS_JABS = 8
HAS_LOCAL = 16
HAS_COM = 32
HAS_FREE = 64
HAS_NARGS = 128

CMP_OP = (
    '<', '<=', '==', '!=', '>', '>=', 'in', 'not in', 'is',
    'is not', 'exception match', 'BAD'
)

OPCODES = {
    1: 'POP_TOP',
    2: 'ROT_TWO',
    3: 'ROT_THREE',
    4: 'DUP_TOP',
    5: 'DUP_TOP_TWO',
    9: 'NOP',
    10: 'UNARY_POSITIVE',
    11: 'UNARY_NEGATIVE',
    12: 'UNARY_NOT',
    15: 'UNARY_INVERT',
    16: 'BINARY_MATRIX_MULTIPLY',  # 16, 17 added newly in 3.5
    17: 'INPLACE_MATRIX_MULTIPLY',
    19: 'BINARY_POWER',
    20: 'BINARY_MULTIPLY',
    22: 'BINARY_MODULO',
    23: 'BINARY_ADD',
    24: 'BINARY_SUBTRACT',
    25: 'BINARY_SUBSCR',
    26: 'BINARY_FLOOR_DIVIDE',
    27: 'BINARY_TRUE_DIVIDE',
    28: 'INPLACE_FLOOR_DIVIDE',
    29: 'INPLACE_TRUE_DIVIDE',
    50: 'GET_AITER',
    51: 'GET_ANEXT',
    52: 'BEFORE_ASYNC_WITH',
    54: 'STORE_MAP',
    55: 'INPLACE_ADD',
    56: 'INPLACE_SUBTRACT',
    57: 'INPLACE_MULTIPLY',
    59: 'INPLACE_MODULO',
    60: 'STORE_SUBSCR',
    61: 'DELETE_SUBSCR',
    62: 'BINARY_LSHIFT',
    63: 'BINARY_RSHIFT',
    64: 'BINARY_AND',
    65: 'BINARY_XOR',
    66: 'BINARY_OR',
    67: 'INPLACE_POWER',
    68: 'GET_ITER',
    69: 'STORE_LOCALS',
    70: 'PRINT_EXPR',
    71: 'LOAD_BUILD_CLASS',
    72: 'YIELD_FROM',  #
    73: 'GET_AWAITABLE',
    75: 'INPLACE_LSHIFT',
    76: 'INPLACE_RSHIFT',
    77: 'INPLACE_AND',
    78: 'INPLACE_XOR',
    79: 'INPLACE_OR',
    80: 'BREAK_LOOP',
    81: 'WITH_CLEANUP',
    82: 'WITH_CLEANUP_FINISH',  # Added newly in 3.5
    83: 'RETURN_VALUE',
    84: 'IMPORT_STAR',
    86: 'YIELD_VALUE',
    87: 'POP_BLOCK',
    88: 'END_FINALLY',
    89: 'POP_EXCEPT',  # BUILD_CLASS in Python 2
    90: 'STORE_NAME',
    91: 'DELETE_NAME',
    92: 'UNPACK_SEQUENCE',
    93: 'FOR_ITER',
    94: 'UNPACK_EX',  # LIST_APPEND in Python 2
    95: 'STORE_ATTR',
    96: 'DELETE_ATTR',
    97: 'STORE_GLOBAL',
    98: 'DELETE_GLOBAL',
    100: 'LOAD_CONST',
    101: 'LOAD_NAME',
    102: 'BUILD_TUPLE',
    103: 'BUILD_LIST',
    104: 'BUILD_SET',
    105: 'BUILD_MAP',
    106: 'LOAD_ATTR',
    107: 'COMPARE_OP',
    108: 'IMPORT_NAME',
    109: 'IMPORT_FROM',
    110: 'JUMP_FORWARD',
    111: 'JUMP_IF_FALSE_OR_POP',
    112: 'JUMP_IF_TRUE_OR_POP',
    113: 'JUMP_ABSOLUTE',
    114: 'POP_JUMP_IF_FALSE',
    115: 'POP_JUMP_IF_TRUE',
    116: 'LOAD_GLOBAL',
    119: 'CONTINUE_LOOP',
    120: 'SETUP_LOOP',
    121: 'SETUP_EXCEPT',
    122: 'SETUP_FINALLY',
    124: 'LOAD_FAST',
    125: 'STORE_FAST',
    126: 'DELETE_FAST',
    130: 'RAISE_VARARGS',
    131: 'CALL_FUNCTION',
    132: 'MAKE_FUNCTION',
    133: 'BUILD_SLICE',
    134: 'MAKE_CLOSURE',
    135: 'LOAD_CLOSURE',
    136: 'LOAD_DEREF',
    137: 'STORE_DEREF',
    138: 'DELETE_DEREF',
    140: 'CALL_FUNCTION_VAR',
    141: 'CALL_FUNCTION_KW',
    142: 'CALL_FUNCTION_VAR_KW',
    143: 'SETUP_WITH',
    144: 'EXTENDED_ARG',
    145: 'LIST_APPEND',
    146: 'SET_ADD',
    147: 'MAP_ADD',
    148: 'LOAD_CLASSDEREF',
    149: 'BUILD_LIST_UNPACK',  # 149 to 153 newly added in 3.5
    150: 'BUILD_MAP_UNPACK',
    151: 'BUILD_MAP_UNPACK_WITH_CALL',
    152: 'BUILD_TUPLE_UNPACK',
    153: 'BUILD_SET_UNPACK',
    154: 'SETUP_ASYNC_WITH',
    160: 'LOAD_METHOD',  # 160, 161 added newly in 3.5
    161: 'CALL_METHOD'
}

# Taken Python-2.5 as base here.
OPCODES_2 = {
    0: 'STOP_CODE'
    1: 'POP_TOP'
    2: 'ROT_TWO'
    3: 'ROT_THREE'
    4: 'DUP_TOP'
    5: 'ROT_FOUR'
    9: 'NOP'
    10: 'UNARY_POSITIVE'
    11: 'UNARY_NEGATIVE'
    12: 'UNARY_NOT'
    13: 'UNARY_CONVERT'
    15: 'UNARY_INVERT'
    18: 'LIST_APPEND'
    19: 'BINARY_POWER'
    20: 'BINARY_MULTIPLY'
    21: 'BINARY_DIVIDE'
    22: 'BINARY_MODULO'
    23: 'BINARY_ADD'
    24: 'BINARY_SUBTRACT'
    25: 'BINARY_SUBSCR'
    26: 'BINARY_FLOOR_DIVIDE'
    27: 'BINARY_TRUE_DIVIDE'
    28: 'INPLACE_FLOOR_DIVIDE'
    29: 'INPLACE_TRUE_DIVIDE'
    30: 'SLICE+0'
    31: 'SLICE+1'
    32: 'SLICE+2'
    33: 'SLICE+3'
    40: 'STORE_SLICE+0'
    41: 'STORE_SLICE+1'
    42: 'STORE_SLICE+2'
    43: 'STORE_SLICE+3'
    50: 'DELETE_SLICE+0'
    51: 'DELETE_SLICE+1'
    52: 'DELETE_SLICE+2'
    53: 'DELETE_SLICE+3'
    55: 'INPLACE_ADD'
    56: 'INPLACE_SUBTRACT'
    57: 'INPLACE_MULTIPLY'
    58: 'INPLACE_DIVIDE'
    59: 'INPLACE_MODULO'
    60: 'STORE_SUBSCR'
    61: 'DELETE_SUBSCR'
    62: 'BINARY_LSHIFT'
    63: 'BINARY_RSHIFT'
    64: 'BINARY_AND'
    65: 'BINARY_XOR'
    66: 'BINARY_OR'
    67: 'INPLACE_POWER'
    68: 'GET_ITER'
    70: 'PRINT_EXPR'
    71: 'PRINT_ITEM'
    72: 'PRINT_NEWLINE'
    73: 'PRINT_ITEM_TO'
    74: 'PRINT_NEWLINE_TO'
    75: 'INPLACE_LSHIFT'
    76: 'INPLACE_RSHIFT'
    77: 'INPLACE_AND'
    78: 'INPLACE_XOR'
    79: 'INPLACE_OR'
    80: 'BREAK_LOOP'
    81: 'WITH_CLEANUP'
    82: 'LOAD_LOCALS'
    83: 'RETURN_VALUE'
    84: 'IMPORT_STAR'
    85: 'EXEC_STMT'
    86: 'YIELD_VALUE'
    87: 'POP_BLOCK'
    88: 'END_FINALLY'
    89: 'BUILD_CLASS'
    90: 'STORE_NAME'
    91: 'DELETE_NAME'
    92: 'UNPACK_SEQUENCE'
    93: 'FOR_ITER'
    95: 'STORE_ATTR'
    96: 'DELETE_ATTR'
    97: 'STORE_GLOBAL'
    98: 'DELETE_GLOBAL'
    99: 'DUP_TOPX'
    100: 'LOAD_CONST'
    101: 'LOAD_NAME'
    102: 'BUILD_TUPLE'
    103: 'BUILD_LIST'
    104: 'BUILD_MAP'
    105: 'LOAD_ATTR'
    106: 'COMPARE_OP'
    107: 'IMPORT_NAME'
    108: 'IMPORT_FROM'
    110: 'JUMP_FORWARD'
    111: 'JUMP_IF_FALSE'
    112: 'JUMP_IF_TRUE'
    113: 'JUMP_ABSOLUTE'
    116: 'LOAD_GLOBAL'
    119: 'CONTINUE_LOOP'
    120: 'SETUP_LOOP'
    121: 'SETUP_EXCEPT'
    122: 'SETUP_FINALLY'
    124: 'LOAD_FAST'
    125: 'STORE_FAST'
    126: 'DELETE_FAST'
    130: 'RAISE_VARARGS'
    131: 'CALL_FUNCTION'
    132: 'MAKE_FUNCTION'
    133: 'BUILD_SLICE'
    134: 'MAKE_CLOSURE'
    135: 'LOAD_CLOSURE'
    136: 'LOAD_DEREF'
    137: 'STORE_DEREF'
    140: 'CALL_FUNCTION_VAR'
    141: 'CALL_FUNCTION_KW'
    142: 'CALL_FUNCTION_VAR_KW'
    143: 'EXTENDED_ARG'

}
OPCODES_2_5 = OPCODES_2.copy()

OPCODES_2_6 = OPCODES_2.copy()
OPCODES_2_6.update({
    54: 'STORE_MAP',
    94: 'LIST_APPEND'
})
OPCODES_2_6.pop(18)  # LIST_APPND has been changed to 94 from 18

OPCODES_3_0 = OPCODES.copy()

OPCODES_3_1 = OPCODES.copy()

OPCODES_3_2 = OPCODES.copy()

OPCODES_3_3 = OPCODES.copy()

OPCODES_3_4 = OPCODES.copy()

OPCODES_3_5 = OPCODES.copy()

# overrrided opcdes in 3.5
OPCODES_3_5.update({
    69: 'GET_YIELD_FROM_ITER',
    81: 'WITH_CLEANUP_START',
})

# Removed opcodes in 3.5
OPCODES_3_5.pop(54)

OPCODES_3_6 = OPCODES_3_5.copy()
OPCODES_3_6.update({
    85: 'SETUP_ANNOTATIONS',
    127: 'STORE_ANNOTATION',
    142: 'CALL_FUNCTION_EX',
    155: 'FORMAT_VALUE',
    156: 'BUILD_CONST_KEY_MAP',
    157: 'BUILD_STRING',
    158: 'BUILD_TUPLE_UNPACK_WITH_CALL'
})

# Removed opcodes in 3.6
OPCODES_3_6.pop(140)

OPCODES_3_7 = OPCODES_3_6.copy()
OPCODES_3_7.update({
    160: 'LOAD_METHOD',
    161: 'CALL_METHOD'
})

HAS_ARGUMENT = 90  # Opcode > 90 have arguments to deal with

# We don't want the name conflict in opcodes module.
EXTENDED_ARG_NAME = 'EXTENDED_ARG'
FORMAT_VALUE_NAME = 'FORMAT_VALUE'
MAKE_FUNCTION_NAME = 'MAKE_FUNCTION'

# Opcodes with name table lookup required.
NAME_OPCODES = (
    90, 91, 95, 96, 97, 98, 101, 106, 108, 109, 116, 160
)

# Opcodes with relative jump.
JREL_OPCODES = (93, 110, 122, 143, 154, 162)

# Opcodes with absolute jimp
JABS_OPCODES = (111, 112, 113, 114, 115)

# Opcodes with constants.
CONST_OPCODES = (100,)

# Opcodes with compare operator.
CMP_OPCODES = (107,)

# Opcodes with local variables involved.
LOCAL_OPCODES = (124, 125, 126)

# Opcodes with free variables involved, like closure.
FREE_OPCODES = (135, 136, 137, 138, 148)

NARGS_OPCODES = (None, )

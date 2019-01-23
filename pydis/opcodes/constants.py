"""Base opcode definitions.
"""

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

OPCODES_3_0 = OPCODES.copy()

OPCODES_3_1 = OPCODES.copy()

OPCODES_3_2 = OPCODES.copy()

OPCODES_3_3 = OPCODES.copy()

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
EXTENDED_ARG_CODE = 144  # Extended argument opcode number.
FORMAT_VALUE_CODE = 155
MAKE_FUNCTION_CODE = 132

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

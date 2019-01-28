from .constants import (
    CMP_OP, HAS_ARGUMENT, EXTENDED_ARG_NAME, FORMAT_VALUE_NAME,
    IS_EXTENDED_ARG, IS_MAKE_FUNCTION, IS_FORMAT_VALUE,
    MAKE_FUNCTION_NAME, OPCODES_3_0, OPCODES_3_4, OPCODES_3_5, OPCODES_3_6,
    OPCODES_3_7,

    # Opcode flags
    HAS_CMP, HAS_CONST, HAS_FREE, HAS_JREL, HAS_JABS, HAS_LOCAL,
    HAS_NAME, HAS_NARGS, HAS_ARG,

    # Opcodes classifications
    CMP_OPCODES, CONST_OPCODES, FREE_OPCODES, JREL_OPCODES,
    JABS_OPCODES, LOCAL_OPCODES, NAME_OPCODES, NARGS_OPCODES,

    PY_VERSION
)

MAKE_FUNCTION_FLAGS = ('defaults', 'kwdefaults', 'annotations', 'closure')


class Opcode:

    # Op code and name are fixed for a given instruction type, hence they would
    # be defined at class level.
    OPCODE = None
    OPCODE_NAME = None
    FLAGS = 0
    PYTHON_VERSION = None

    def __init__(
        self,
        offset,
        end,
        line,
        arg,
        arg_val,
        arg_repr,
        is_jump_target):

        self.offset = offset
        self.end = end
        self.line = line
        self.arg = arg
        self.arg_val = arg_val
        self.arg_repr = arg_repr
        self.is_jump_target = is_jump_target

    def __repr__(self):
        return self.__class__.__name__

    @classmethod
    def has_const(cls):
        return cls.FLAGS & HAS_CONST

    @classmethod
    def has_name(cls):
        return cls.FLAGS & HAS_NAME

    @classmethod
    def has_jrel(cls):
        return cls.FLAGS & HAS_JREL

    @classmethod
    def has_jabs(cls):
        return cls.FLAGS & HAS_JABS

    @classmethod
    def has_jump(cls):
        return cls.FLAGS & (HAS_JREL | HAS_JABS)

    @classmethod
    def has_local(cls):
        return cls.FLAGS & HAS_LOCAL

    @classmethod
    def has_free(cls):
        return cls.FLAGS & HAS_FREE

    @classmethod
    def has_nargs(cls):
        return cls.FLAGS & HAS_NARGS

    @classmethod
    def has_arg(cls):
        return cls.FLAGS & HAS_ARG

    @classmethod
    def has_cmp(cls):
        return cls.FLAGS & HAS_CMP

    @classmethod
    def is_extended_arg(cls):
        return cls.FLAGS & IS_EXTENDED_ARG

    @classmethod
    def is_format_value(cls):
        return cls.FLAGS & IS_FORMAT_VALUE

    @classmethod
    def is_make_function(cls):
        return cls.FLAGS & IS_MAKE_FUNCTION


class OpcodeClassFactory:

    opcodes_generated = False
    opcodes_version = None

    @classmethod
    def gen_opcode_classes(cls, python_version=PY_VERSION):
        # If they are already generated, then no need to do it again.
        if cls.opcodes_generated and cls.opcodes_version == python_version:

            return
        # If no version passed, then consider default python 3 opcodes.
        ops = globals().get(
            'OPCODES_%s_%s' % tuple(str(python_version).split('.')))

        globals()['OPCODE_MAPPER'] = ops
        for op_code, op_name_flag in ops.items():
            op_name, flag = op_name_flag
            op_cls = type(
                op_name,
                (Opcode, ),
                {
                    'OPCODE': op_code,
                    'OPCODE_NAME': op_name,
                    'PYTHON_VERSION': python_version,
                    'FLAGS': flag
                }
            )
            globals()[op_name] = op_cls

        cls.opcodes_generated = True
        cls.opcodes_version = python_version

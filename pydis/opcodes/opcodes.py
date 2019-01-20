from .constants import (
    CMP_OP, HAS_ARGUMENT, EXTENDED_ARG, OPCODES_3_0, OPCODES_3_5, OPCODES_3_6,
    OPCODES_3_7,

    # Opcode flags
    HAS_COM, HAS_CONST, HAS_FREE, HAS_JREL, HAS_JABS, HAS_LOCAL,
    HAS_NAME, HAS_NARGS,

    # Opcodes classifications
    CMP_OPCODES, CONST_OPCODES, FREE_OPCODES, JREL_OPCODES,
    JABS_OPCODES, LOCAL_OPCODES, NAME_OPCODES, NARGS_OPCODES
)


class Opcode:

    OP_CODE = None

    def __init__(self, index, line):
        self.index = index
        self.line = line
        self.target = None
        self.code = None

    def __repr__(self):
        return self.__class__.__name__

    @classmethod
    def has_const(cls):
        return cls.OP_CODE in CONST_OPCODES

    @classmethod
    def has_name(cls):
        return cls.OP_CODE in NAME_OPCODES

    @classmethod
    def has_jrel(cls):
        return cls.OP_CODE in JREL_OPCODES

    @classmethod
    def has_jabs(cls):
        return cls.OP_CODE in JABS_OPCODES

    @classmethod
    def has_jump(cls):
        return cls.OP_CODE in (JABS_OPCODES + JREL_OPCODES)

    @classmethod
    def has_local(cls):
        return cls.OP_CODE in LOCAL_OPCODES

    @classmethod
    def has_free(cls):
        return cls.OP_CODE in FREE_OPCODES

    @classmethod
    def has_nargs(cls):
        return cls.OP_CODE in NARGS_OPCODES

    @classmethod
    def has_arg(cls):
        return cls.OP_CODE >= HAS_ARGUMENT


class OpcodeClassFactory:

    @classmethod
    def gen_opcode_classes(self, python_version=(3, 0)):

        # If no version passed, then consider default python 3 opcodes.
        ops = globals().get('OPCODES_%s_%s' % python_version)
        for op_code, op_name in ops.items():
            op_cls = type(op_name, (Opcode, ), {'OP_CODE': op_code})
            globals()[op_name] = op_cls

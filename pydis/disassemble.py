# Copyright (c) 2018 by Srinivas Garlapati

"""Disassemble the code object, it would be in multiple ways. Show the
disassembled instructions or return the sequence of instructions from the
bytecode sequence.
"""

from pydis.marshal import load


def get_line_sequence(code):

    addr = 0  # Address start with byte index zero.
    last_lineno = None

    # co_lnotab is an array of unsigned bytes, which hols differences in
    # bytecode and line number increments or decrements with the previous
    # instruction.
    #
    # TODO: Add more explanation here

    lineno = code.co_firstlineno
    byte_increments = code.co_lnotab[0::2]
    line_increments = code.co_lnotab[1::2]

    for byte_incr, line_incr in zip(byte_increments, line_increments):
        if byte_incr:
            if last_lineno != line_incr:
                yield (addr, lineno)
                last_lineno = lineno
            addr += byte_incr

        lineno += line_incr
        if line_incr >= 0x80:
            # Line increments are 8 bit signed integers, if the number is gone
            # beyod 128, this will bring inbetween the range.
            line_incr -= 0x100

    yield(addr, lineno)


def get_labels():
    pass


class Instruction:

    def _disassemble(self):
        pass
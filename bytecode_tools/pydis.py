# Copyright (c) 2018-2019 by Srinivas Garlapati

"""Disassemble the code object, it would be in multiple ways. Show the
disassembled instructions or return the sequence of instructions from the
bytecode sequence.

This is more relavent to/used some portions of Cpython's Lib/dis.py


"""
# pylint: disable=E1101, R0902, C0103, R0912

import sys
import types

from bytecode_tools.common import opcodes
from bytecode_tools.common.constants import PY_VERSION
from bytecode_tools.common.decode_code_object import DecodeCodeObject


# These are fixed as per Cpython's Lib/dis.py
_OPNAME_WIDTH = 20
_OPARG_WIDTH = 5

_have_code = (types.MethodType, types.FunctionType, types.CodeType,
              classmethod, staticmethod, type)


def _try_compile(source, name):
    """Attempts to compile the given source, first as an expression and
       then as a statement if the first approach fails.

       Utility function to accept strings in functions that otherwise
       expect code objects
    """
    try:
        c = compile(source, name, 'eval')
    except SyntaxError:
        c = compile(source, name, 'exec')
    return c


def dis(x=None, file=None, depth=None):
    """Disassemble classes, methods, functions, and other compiled objects.

    With no argument, disassemble the last traceback.

    Compiled objects currently include generator objects, async generator
    objects, and coroutine objects, all of which store their code object
    in a special attribute.
    """
    if x is None:
        distb(file=file)
        return
    # Extract functions from methods.
    if hasattr(x, '__func__'):
        x = x.__func__
    # Extract compiled code objects from...
    if hasattr(x, '__code__'):  # ...a function, or
        x = x.__code__
    elif hasattr(x, 'gi_code'):  #...a generator object, or
        x = x.gi_code
    elif hasattr(x, 'ag_code'):  #...an asynchronous generator object, or
        x = x.ag_code
    elif hasattr(x, 'cr_code'):  #...a coroutine.
        x = x.cr_code
    # Perform the disassembly.
    if hasattr(x, '__dict__'):  # Class or module
        items = sorted(x.__dict__.items())
        for name, x1 in items:
            if isinstance(x1, _have_code):
                print("Disassembly of %s:" % name)
                try:
                    dis(x1, file=file, depth=depth)
                except TypeError as msg:
                    print("Sorry:", msg)
                print('')
    elif hasattr(x, 'co_code'): # Code object
        disassemble_recursive(x, file=file, depth=depth)
    elif isinstance(x, str):    # Source code
        _disassemble_str(x, file=file, depth=depth)
    elif isinstance(x, (bytes, bytearray)): # Raw bytecode
        disassemble(x, file=file)
    else:
        raise TypeError("don't know how to disassemble %s objects" %
                        type(x).__name__)

def _disassemble_str(source, **kwargs):
    """Compile the source string, then disassemble the code object."""
    disassemble_recursive(_try_compile(source, '<dis>'), **kwargs)


def distb(tb=None, file=None):
    """Disassemble a traceback (default: last traceback).

    tb: Traceback can be provided, else it  takes the last traceback.
    """
    if tb is None:
        try:
            tb = sys.last_traceback
        except AttributeError:
            raise RuntimeError("no last traceback to disassemble")
        while tb.tb_next:
            tb = tb.tb_next

    # Lats traceback always would be the current version of python, hence no
    # need to worry about the python version.
    disassemble(tb.tb_frame.f_code, tb.tb_lasti, file=file)


def disassemble_recursive(
        code, lasti=-1, python_version=None, file=None, depth=None):
    """Disassemble a code object recursively"""
    disassemble(code, lasti, python_version, file)

    # if the depth is 0 then no need to proceed.
    if depth is None or depth > 0:
        # For the next turn, depth should be reduced by one.
        if depth is not None:
            depth -= 1
        for obj in code.co_consts:
            if hasattr(obj, 'co_code'):
                print()
                print("Disassembly of %r:" % (code,))
                disassemble_recursive(
                    obj, lasti, python_version, file, depth
                )


def disassemble(code, lasti=-1, python_version=None, file=None):
    """Disassemble a code object."""
    DecodeCodeObject(
        code,
        last_instruction=lasti,
        python_version=python_version,
        file=file
    ).disassemble()


def instructions(code, python_version=None):
    """Disassemble a code object."""
    return DecodeCodeObject(
        code,
        python_version=python_version
    ).unpack_code()
# Copyright (c) 2018 by Srinivas Garlapati


from pydis.marshal.load import load


FLAG_REF = 0x80

MARSHAL_CODES = {
    0x30: 'null',
    0x4e: 'none',
    0x46: 'false',
    0x54: 'true',
    0x53: 'stopiter',
    0x2e: 'elipsis',
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


__all__ = [load]
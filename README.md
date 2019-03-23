
[![Build Status](https://travis-ci.com/gsb-eng/bytecode_tools.svg?branch=master)](https://travis-ci.com/gsb-eng/bytecode_tools)
[![Coverage Status](https://img.shields.io/codecov/c/github/gsb-eng/bytecode_tools/master.svg)](https://codecov.io/github/gsb-eng/bytecode_tools?branch=master)
<br />

Bytecode Tools
===============

Bytecode tools are combination of multiple necessary modules to play with Python
bytecode.

Right now it has `pydis`.

What is pydis?
=========

`pydis` is a python disassembler, it can be a drop in replacement for cpython's
`Lib/dis.py`.

Pydis supports all the cpython versions above 2.5, every verion above 2.5
supports other versions. This means, pydis decodes 2.6 bytes code in 3.6 and
vice versa.

Why pydis?
==========

Python's `dis` moduel is super helpful for looking inside code objects, but it
won't support other python versions. If the code object is created through
`python 3.5` and try to disassemble with `python3.6`, it won't work.

Each python version gets changes to opcodes, there will be ne ones added and few
are deleted. Unless you recreate the code object with new python version, the
same code object can't be interpreted with old versions.

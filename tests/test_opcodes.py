
import os
import sys
import unittest

from bytecode_tools.constants import IS_PY2
from bytecode_tools import opcodes



class TestPycDecoder(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.pyc_dir = os.path.join(self.base_dir, 'pyc_files')
        self.pyc36 = os.path.join(self.pyc_dir, 'test.cpython-36.pyc')
        self.pyc37 = os.path.join(self.pyc_dir, 'test.cpython-37.pyc')

    def test_opcode(self):
        clas = opcodes.Opcode
        clas.OPCODE = 144
        clas.OPCODE_NAME = 'EXTENDED_ARG'
        clas.FLAGS = 640
        clas.PYTHON_VERSION = 3.7
        self.assertEqual(clas.is_extended_arg(), 512)
        self.assertNotEqual(clas.has_arg(), 0)
        self.assertEqual(repr(clas(1, 2, 3, 4, 5, 6, 7)), 'Opcode')

        clas.OPCODE = 90
        clas.FLAGS = 130
        self.assertNotEqual(clas.has_name(), 0)

        clas.OPCODE = 100
        clas.FLAGS = 129
        self.assertNotEqual(clas.has_const(), 0)

        clas.OPCODE = 122
        clas.FLAGS = 132
        self.assertNotEqual(clas.has_jrel(), 0)
        self.assertNotEqual(clas.has_jump(), 0)

        clas.OPCODE = 112
        clas.FLAGS = 136
        self.assertNotEqual(clas.has_jabs(), 0)
        self.assertNotEqual(clas.has_jump(), 0)

        clas.OPCODE = 124
        clas.FLAGS = 144
        self.assertNotEqual(clas.has_local(), 0)

        clas.OPCODE = 136
        clas.FLAGS = 192
        self.assertNotEqual(clas.has_free(), 0)

        clas.OPCODE = 107
        clas.FLAGS = 160
        self.assertNotEqual(clas.has_cmp(), 0)

        clas.OPCODE = 132
        clas.FLAGS = 1024
        self.assertNotEqual(clas.is_make_function(), 0)

        clas.OPCODE = 132
        clas.FLAGS = 2048
        self.assertNotEqual(clas.is_format_value(), 0)

        clas.OPCODE = 132
        clas.FLAGS = 256
        self.assertNotEqual(clas.has_nargs(), 0)


    def test_opcode_class_factory_37(self):
        opcodes.OpcodeClassFactory.gen_opcode_classes(3.7)
        self.assertEqual(len(opcodes.OpcodeClassFactory.opcode_register), 121)

        # Do not generate if opcodes are already generated
        ret = opcodes.OpcodeClassFactory.gen_opcode_classes(3.7)
        self.assertEqual(ret, 403)

    def test_opcode_class_factory_36(self):
        opcodes.OpcodeClassFactory.gen_opcode_classes(3.6)
        self.assertEqual(len(opcodes.OpcodeClassFactory.opcode_register), 121)

    def test_opcode_class_factory_35(self):
        opcodes.OpcodeClassFactory.gen_opcode_classes(3.5)
        self.assertEqual(len(opcodes.OpcodeClassFactory.opcode_register), 116)

    def test_opcode_class_factory_34(self):
        opcodes.OpcodeClassFactory.gen_opcode_classes(3.4)
        self.assertEqual(len(opcodes.OpcodeClassFactory.opcode_register), 117)

    def test_opcode_class_factory_27(self):
        opcodes.OpcodeClassFactory.gen_opcode_classes(2.7)
        self.assertEqual(len(opcodes.OpcodeClassFactory.opcode_register), 119)

        # Do not generate if opcodes are already generated
        ret = opcodes.OpcodeClassFactory.gen_opcode_classes(2.7)
        self.assertEqual(ret, 403)

    def test_opcode_extended_arg_37(self):
        opcodes.OpcodeClassFactory.gen_opcode_classes(3.7)
        self.assertEqual(len(opcodes.OpcodeClassFactory.opcode_register), 121)

        # Do not generate if opcodes are already generated
        self.assertEqual(opcodes.EXTENDED_ARG.OPCODE, 144)
        self.assertEqual(opcodes.EXTENDED_ARG.OPCODE_NAME, 'EXTENDED_ARG')
        self.assertTrue(opcodes.EXTENDED_ARG.is_extended_arg())

    def test_opcode_extended_arg_27(self):
        opcodes.OpcodeClassFactory.gen_opcode_classes(2.7)
        self.assertEqual(len(opcodes.OpcodeClassFactory.opcode_register), 119)

        # Do not generate if opcodes are already generated
        self.assertEqual(opcodes.EXTENDED_ARG.OPCODE, 145)
        self.assertEqual(opcodes.EXTENDED_ARG.OPCODE_NAME, 'EXTENDED_ARG')
        self.assertTrue(opcodes.EXTENDED_ARG.is_extended_arg())

    def test_opcode_extended_arg_26(self):
        opcodes.OpcodeClassFactory.gen_opcode_classes(2.6)
        self.assertEqual(len(opcodes.OpcodeClassFactory.opcode_register), 113)

        # Do not generate if opcodes are already generated
        self.assertEqual(opcodes.EXTENDED_ARG.OPCODE, 143)
        self.assertEqual(opcodes.EXTENDED_ARG.OPCODE_NAME, 'EXTENDED_ARG')
        self.assertTrue(opcodes.EXTENDED_ARG.is_extended_arg())


if __name__ == '__main__':
    unittest.main()

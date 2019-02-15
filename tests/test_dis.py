
import os
import sys
import unittest

from bytecode_tools import dis
from bytecode_tools.constants import IS_PY2
from bytecode_tools.pyc_decoder import decode_pyc



class TestPycDecoder(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.pyc_dir = os.path.join(self.base_dir, 'pyc_files')
        self.pyc36 = os.path.join(self.pyc_dir, 'test.cpython-36.pyc')
        self.pyc37 = os.path.join(self.pyc_dir, 'test.cpython-37.pyc')

    def test_unpack(self):
        _, _, _, code_object = decode_pyc(self.pyc37)

        instructions = dis.DecodeCodeObject(
            code_object,
            last_instruction=None,
            python_version=code_object.python_version,
            file=''
        ).unpack_code()

        self.assertEqual(len(instructions), 17)


if __name__ == '__main__':
    unittest.main()

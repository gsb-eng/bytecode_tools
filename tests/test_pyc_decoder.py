
import os
import unittest

from bytecode_tools.common.utils import write_to_file
from bytecode_tools.pycdecode import pycdecode, showpyc
from bytecode_tools.unmarshal import CodeType


class TestPycDecoder(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.pyc_dir = os.path.join(self.base_dir, 'pyc_files')
        self.pyc36 = os.path.join(self.pyc_dir, 'test.cpython-36.pyc')
        self.pyc37 = os.path.join(self.pyc_dir, 'test.cpython-37.pyc')
        self.temp_file = os.path.join(self.pyc_dir, 'temp_file.txt')

    def test_decode_pyc_36(self):

        self.assertTrue(os.path.exists(self.pyc36))

        ret_val = pycdecode(self.pyc36)

        self.assertEqual(len(ret_val), 4)
        self.assertEqual(ret_val[0], 3379)
        self.assertEqual(ret_val[2], 220)
        self.assertIsInstance(ret_val[3], CodeType)

    def test_decode_pyc_37(self):

        self.assertTrue(os.path.exists(self.pyc37))
        ret_val = pycdecode(self.pyc37)
        self.assertEqual(len(ret_val), 4)
        self.assertEqual(ret_val[0], 3394)
        self.assertEqual(ret_val[2], 89)
        self.assertIsInstance(ret_val[3], CodeType)

    def test_showpyc_pyc_37(self):
        self.assertTrue(os.path.exists(self.pyc37))
        with open(self.temp_file, 'w') as out:
            with write_to_file(out):
                ret_val = showpyc(self.pyc37)

        with open(self.temp_file, 'r') as file_read:
            magic_line = file_read.readline()
            magic_line = magic_line.split(':')
            self.assertEqual(magic_line[0].strip(), 'Magic')
            self.assertEqual(magic_line[1].strip(), '3394')

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)


if __name__ == '__main__':
    unittest.main()

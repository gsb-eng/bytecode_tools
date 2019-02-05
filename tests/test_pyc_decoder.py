
import os
import unittest

from pydis.pyc_decoder import decode_pyc
from pydis.unmarshal import CodeType


class TestPycDecoder(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.pyc_dir = os.path.join(self.base_dir, 'pyc_files')
        self.pyc36 = os.path.join(self.pyc_dir, 'test.cpython-36.pyc')
        self.pyc37 = os.path.join(self.pyc_dir, 'test.cpython-37.pyc')

    def test_decode_pyc_36(self):

        self.assertTrue(os.path.exists(self.pyc36))

        ret_val = decode_pyc(self.pyc36)

        self.assertEqual(len(ret_val), 4)
        self.assertEqual(ret_val[0], 3379)
        self.assertEqual(ret_val[2], 220)
        self.assertIsInstance(ret_val[3], CodeType)

    def test_decode_pyc_37(self):

        self.assertTrue(os.path.exists(self.pyc37))
        ret_val = decode_pyc(self.pyc37)
        self.assertEqual(len(ret_val), 4)
        self.assertEqual(ret_val[0], 3394)
        self.assertEqual(ret_val[2], 89)
        self.assertIsInstance(ret_val[3], CodeType)


if __name__ == '__main__':
    unittest.main()

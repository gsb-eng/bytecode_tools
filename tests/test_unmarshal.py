
import os
import unittest

from bytecode_tools.unmarshal import load, loads, CodeType
from bytecode_tools.unmarshal import CodeType


class TestPycDecoder(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.pyc_dir = os.path.join(self.base_dir, 'pyc_files')
        self.pyc36 = os.path.join(self.pyc_dir, 'test.cpython-36.pyc')
        self.pyc37 = os.path.join(self.pyc_dir, 'test.cpython-37.pyc')

    def test_loads(self):
        self.assertEqual(loads(b'N'), None)
        self.assertEqual(loads(b'.'), Ellipsis)
        self.assertEqual(loads(b'F'), False)
        self.assertEqual(loads(b'T'), True)
        self.assertEqual(loads(b'S'), StopIteration)

    def test_load_int(self):
        self.assertEqual(loads(b'i\1\0\0\0'), 1)
        self.assertEqual(loads(b'i\0\0\0\x81'), -2130706432)
        self.assertEqual(loads(b'i\0\0\0\0'), 0)

    def test_load_float(self):
        self.assertEqual(loads(b'f\x030.1'), 0.1)
        self.assertEqual(loads(b'f\x010.0'), 0)

    def test_load_binary_float(self):
        self.assertEqual(loads(b'g\0\0\0\0\0\0\xf8\x3f'), 1.5)
        self.assertEqual(loads(b'g\0\0\0\0\0\0\xe0\xbf'), -0.5)

    def test_load_int64(self):
        self.assertEqual(loads(b'I\1\0\0\0\0\0\0\0'), 1)
        self.assertEqual(loads(b'I\0\0\0\0\0\0\0\x80'), -9223372036854775808)
        self.assertEqual(loads(b'I\0\0\0\0\0\0\0\0'), 0)
        self.assertEqual(
            loads(b'I\xff\xff\xff\xff\xff\xff\xff\0'), 72057594037927935)

    def test_load_long(self):
        self.assertEqual(loads(b'l\7\0\0\0\ud620\u3bdf\u7b83\u5a46\u3cea\u43d6\ub000'), 14273427342342384723428347234)
        self.assertEqual(loads(b'l\xf9\xff\xff\xff\0\0\4\0\2\0\5\0'), 175924008058880)

    def test_load_complex(self):
        self.assertEqual(loads(b'x\2.1\6.12345'), 0.1+0.12345j)

    def test_load_binary_complex(self):
        self.assertEqual(
            loads(b'y\0\0\0\0\0\0\xf8\x3f\0\0\0\0\0\0\xe0\xbf'), 1.5+-0.5j)




if __name__ == '__main__':
    unittest.main()

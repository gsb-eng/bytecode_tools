
import os
import sys
import unittest

from bytecode_tools.common.constants import IS_PY2
from bytecode_tools.unmarshal import load, loads, CodeType
from bytecode_tools.unmarshal import CodeType



class TestPycDecoder(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.pyc_dir = os.path.join(self.base_dir, 'pyc_files')
        self.pyc36 = os.path.join(self.pyc_dir, 'test.cpython-36.pyc')
        self.pyc37 = os.path.join(self.pyc_dir, 'test.cpython-37.pyc')

    def test_bad_code(self):
        with self.assertRaises(ValueError):
            loads(b'$')
            loads(b'1223')

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
        self.assertEqual(
            loads(b'l\x07\x00\x00\x00b\r\xdf;\x83{FZ\xea<\xd6C\x0b\x00'),
            14273427342342384723428347234)
        self.assertEqual(
            loads(b'l\xf9\xff\xff\xffb\r\xdf;\x83{FZ\xea<\xd6C\x0b\x00'),
            -14273427342342384723428347234)

    def test_load_complex(self):
        self.assertEqual(loads(b'x\2.1\6.12345'), 0.1+0.12345j)

    def test_load_binary_complex(self):
        self.assertEqual(
            loads(b'y\0\0\0\0\0\0\xf8\x3f\0\0\0\0\0\0\xe0\xbf'), 1.5+-0.5j)

    def test_load_string(self):
        assert loads(b's\5\0\0\0hello', 2.6) == 'hello'
        assert loads(b's\5\0\0\0hello', 2.7) == 'hello'
        assert loads(b's\5\0\0\0hello', 3.4) == b'hello'
        assert loads(b's\5\0\0\0hello', 3.5) == b'hello'
        assert loads(b's\5\0\0\0hello', 3.6) == b'hello'
        assert (loads(b's\5\0\0\0hello', 3.7) == b'hello')

    def test_load_interned(self):
        assert loads(b't\5\0\0\0hello', 2.6) == 'hello'
        assert loads(b't\5\0\0\0hello', 2.7) == 'hello'
        assert loads(b't\5\0\0\0hello', 3.4) == 'hello'
        assert loads(b't\5\0\0\0hello', 3.5) == 'hello'
        assert loads(b't\5\0\0\0hello', 3.6) == 'hello'
        assert loads(b't\5\0\0\0hello', 3.7) == 'hello'

    def test_load_stringref(self):
        self.assertEqual(
            loads(b'[\2\0\0\0t\5\0\0\0helloR\0\0\0\0'), ['hello', 'hello'])
        self.assertEqual(
            loads(b'[\3\0\0\0t\5\0\0\0hellot\5\0\0\0worldR\1\0\0\0'),
            ['hello', 'world', 'world'])

    def test_load_tuple(self):
        self.assertEqual(loads(b'(\2\0\0\0i\1\0\0\0i\2\0\0\0'), (1, 2))

    def test_load_list(self):
        self.assertEqual(
            loads(b'[\3\0\0\0i\1\0\0\0i\2\0\0\0i\3\0\0\0'), [1, 2, 3])

    def test_load_dict(self):
        self.assertEqual(
            loads(b'{i\1\0\0\0i\2\0\0\0i\3\0\0\0i\4\0\0\0N'), {1: 2, 3: 4})

    def test_load_small_tuple(self):
        self.assertEqual(loads(b')\2i\1\0\0\0i\2\0\0\0'), (1, 2))

    def test_load_set(self):
        self.assertEqual(
            loads(b'<\3\0\0\0i\1\0\0\0i\2\0\0\0i\3\0\0\0'), set([1, 2, 3]))

    def test_load_frozenset(self):
        self.assertEqual(
            loads(b'>\3\0\0\0i\1\0\0\0i\2\0\0\0i\3\0\0\0'), frozenset([1, 2, 3]))

    def test_load_unicode(self):
        self.assertEqual(loads(b'u\3\0\0\0abc'), 'abc')

        if IS_PY2:
            self.assertEqual(loads(b'u\3\0\0\0a\xc3\xa5'), u'a\xe5')
        else:
            self.assertEqual(loads(b'u\3\0\0\0a\xc3\xa5'), 'a\xe5')

    def test_load_ref(self):
        self.assertEqual(loads(b'(\2\0\0\0\xe9\1\0\0\0r\0\0\0\0'), (1, 1))

    def test_load_ascii(self):
        self.assertEqual(loads(b'a\2\0\0\0ab'), 'ab')
        self.assertEqual(loads(b'a\5\0\0\0aaaaa'), 'a'*5)

    def test_load_ascii_interned(self):
        self.assertEqual(loads(b'A\2\0\0\0ab'), 'ab')
        self.assertEqual(loads(b'A\5\0\0\0aaaaa'), 'a'*5)

    def test_load_short_ascii(self):
        self.assertEqual(loads(b'z\2ab'), 'ab')
        self.assertEqual(loads(b'z\5aaaaa'), 'a'*5)

    def test_load_short_ascii_interned(self):
        self.assertEqual(loads(b'Z\2ab'), 'ab')
        self.assertEqual(loads(b'Z\5aaaaa'), 'a'*5)


if __name__ == '__main__':
    unittest.main()

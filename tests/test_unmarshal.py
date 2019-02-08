
import os
import unittest

from pydis.unmarshal import load, loads, CodeType
from pydis.unmarshal import CodeType


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


if __name__ == '__main__':
    unittest.main()

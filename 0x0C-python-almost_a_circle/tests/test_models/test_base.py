#!/usr/bin/python3
"""
Unittest for base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Testbaseclass(unittest.TestCase):

    def testcreateelems(self):
        b = Base()
        b1 = Base(76)
        b2 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 76)
        self.assertEqual(b2.id, 2)

if __name__ == "__main__":
    unittest.main()

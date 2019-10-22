#!/usr/bin/python3
"""
Unittest for base class
"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Testbaseclass(unittest.TestCase):
    """ test for base"""
    def testcreateelems(self):
        b = Base()
        b1 = Base(76)
        b2 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 76)
        self.assertEqual(b2.id, 2)

    def testsetid(self):
        """ test for set id"""
        b = Base("h")
        b1 = Base({1: 2})
        b2 = Base((1, 4))
        b3 = Base([3, 6])
        b4 = Base(None)
        b5 = Base(0)
        self.assertEqual(b.id, "h")
        self.assertEqual(b1.id, {1: 2})
        self.assertEqual(b2.id, (1, 4))
        self.assertEqual(b3.id, [3, 6])
        self.assertEqual(b4.id, 4)
        self.assertEqual(b5.id, 0)

#     --------- private attribute of class --------

    def testprivate(self):
        """ test for private attribute"""
        b = Base()
        with self.assertRaises(AttributeError):
            b.__nb_objects

#    -------------- static method to_json_string -----------

    def testtojson(self):
        """ test to json"""
        dic = {'id': 8, 'size': 5, 'x': 6, 'y': 7}
        stdic = json.dumps([dic])
        self.assertEqual(Base.to_json_string([dic]), stdic)
        r = Base.to_json_string(None)
        self.assertEqual(r, "[]")
        r = Base.to_json_string([])
        self.assertEqual(r, "[]")
        dic = [1, 2, 3]
        r = Base.to_json_string([dic])
        self.assertEqual(r, "[[1, 2, 3]]")

        dic = {'id': 8, 'size': 5, 'x': 6, 'y': 7}
        stdic = json.dumps([dic])
        self.assertEqual(Rectangle.to_json_string([dic]), stdic)
        r = Rectangle.to_json_string(None)
        self.assertEqual(r, "[]")
        r = Rectangle.to_json_string([])
        self.assertEqual(r, "[]")
        dic = [1, 2, 3]
        r = Rectangle.to_json_string([dic])
        self.assertEqual(r, "[[1, 2, 3]]")

        dic = {'id': 8, 'size': 5, 'x': 6, 'y': 7}
        stdic = json.dumps([dic])
        self.assertEqual(Square.to_json_string([dic]), stdic)
        r = Square.to_json_string(None)
        self.assertEqual(r, "[]")
        r = Square.to_json_string([])
        self.assertEqual(r, "[]")
        dic = [1, 2, 3]
        r = Square.to_json_string([dic])
        self.assertEqual(r, "[[1, 2, 3]]")


    def testtojson(self):
        """error json"""
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Rectangle.to_json_string()
        with self.assertRaises(TypeError):
            Square.to_json_string()
# ------------------ pep8 ----------------------------------
def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['file1.py', 'file2.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

#!/usr/bin/python3
"""
Unittest for Rectangle Class
"""
from io import StringIO
from unittest.mock import patch
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def testcreateelems(self):
        r = Rectangle(1, 1)
        r1 = Rectangle(2, 5, 6)
        r2 = Rectangle(6, 8, 10, 9)
        r3 = Rectangle(1, 1, 1, 1, 90)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r2.width, 6)
        self.assertEqual(r2.height, 8)
        self.assertEqual(r2.x, 10)
        self.assertEqual(r2.y, 9)
        self.assertEqual(r3.id, 90)

    def testgetandset(self):
        r = Rectangle(5, 2)
        self.assertEqual(r.width, 5)
        r.width = 9
        self.assertEqual(r.width, 9)
        self.assertEqual(r.height, 2)
        r.height = 8
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 0)
        r.x = 8
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 0)
        r.y = 1
        self.assertEqual(r.y, 1)
        r.id = 99
        self.assertEqual(r.id, 99)

#  ---------- tests for width -----------------------

    def testwidth(self):
        with self.assertRaises(TypeError):
            r = Rectangle("hola", 2)

        with self.assertRaises(TypeError):
            r = Rectangle([1, 4], 2)

        with self.assertRaises(TypeError):
            r = Rectangle((1, 1), 4)

        with self.assertRaises(TypeError):
            r = Rectangle({'a': 3}, 5)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 6)

        with self.assertRaises(ValueError):
            r = Rectangle(-6, 8)

        with self.assertRaises(TypeError):
            r = Rectangle(3.6, 9)

#   ---------- tests for height -----------------------

    def testheight(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, "hola")

        with self.assertRaises(TypeError):
            r = Rectangle(2, [1, 2])

        with self.assertRaises(TypeError):
            r = Rectangle(4, (1, 2))

        with self.assertRaises(TypeError):
            r = Rectangle(5, {'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Rectangle(6, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(6, -8)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 9.7)

#   ---------- tests for x -----------------------------
    def testx(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, "hola")

        with self.assertRaises(TypeError):
            r = Rectangle(2, 1, [1, 2])

        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, (1, 2))

        with self.assertRaises(TypeError):
            r = Rectangle(5, 6, {'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Rectangle(6, 6, -8)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 2, 9.7)

    def testx1(self):
        r = Rectangle(6, 5, 0)
        self.assertEqual(r.x, 0)


#   ---------- tests for y -------------------------------

    def testy(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, 5, "hola")

        with self.assertRaises(TypeError):
            r = Rectangle(2, 1, 5, [1, 2])

        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 6, (1, 2))

        with self.assertRaises(TypeError):
            r = Rectangle(5, 6, 7, {'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Rectangle(6, 6, 9, -8)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 8, 3, 9.7)

    def testy1(self):
        r = Rectangle(6, 5, 0, 0)
        self.assertEqual(r.y, 0)

#    ---------------------- id ----------------------------

    def testid(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 6)
        r = Rectangle(2, 3, 4, 5, "6")
        self.assertEqual(r.id, "6")
        r = Rectangle(2, 3, 4, 5, {'id': 3})
        self.assertEqual(r.id, {'id': 3})
        r = Rectangle(2, 3, 4, 5, (1, 2))
        self.assertEqual(r.id, (1, 2))
        r = Rectangle(2, 3, 4, 5, [2, 4])
        self.assertEqual(r.id, [2, 4])

#    -----------  Area    ---------------------------------

    def testarea1(self):
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)

    def testarea2(self):
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError):
            r.area(1)

#    ------------- Display ---------------------------------

    def testdisplay(self):
        with patch('sys.stdout', new=StringIO()) as salida:
            r = Rectangle(2, 3)
            r.display()
            st = "##\n##\n##\n"
            self.assertEqual(salida.getvalue(), st)

        with patch('sys.stdout', new=StringIO()) as salida:
            r = Rectangle(2, 3, 2)
            r.display()
            st = "  ##\n  ##\n  ##\n"
            self.assertEqual(salida.getvalue(), st)

        with patch('sys.stdout', new=StringIO()) as salida:
            r = Rectangle(2, 3, 2, 2)
            r.display()
            st = "\n\n  ##\n  ##\n  ##\n"
            self.assertEqual(salida.getvalue(), st)

    def testdisplay1(self):
        r = Rectangle(1, 3)
        with self.assertRaises(TypeError):
            r.display(1)

#    -------------- __str__ ---------------------------------

    def tesstr(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

#    ----------------- Update -------------------------------

    def testupdate(self):
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")
        r.update(2, 2)
        self.assertEqual(str(r), "[Rectangle] (2) 1/1 - 2/1")

        lista = [3, 4, 5]
        r.update(*lista)
        self.assertEqual(str(r), "[Rectangle] (3) 1/1 - 4/5")

        lista = (1, 2, 4, 5)
        r.update(*lista)
        self.assertEqual(str(r), "[Rectangle] (1) 5/1 - 2/4")

        lista = []
        r.update(*lista)
        self.assertEqual(str(r), "[Rectangle] (1) 5/1 - 2/4")

        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 5/1 - 2/4")

        di = {'x': 10, 'y': 20}
        r.update(**di)
        self.assertEqual(str(r), "[Rectangle] (1) 10/20 - 2/4")

        di = {'id': 5, 'width': 5, 'height': 5, 'x': 5, 'y': 5}
        r.update(**di)
        self.assertEqual(str(r), "[Rectangle] (5) 5/5 - 5/5")

        lista = [9, 9, 9, 9, 9]
        dic = {'id': 2, 'width': 2, 'height': 2, 'x': 2, 'y': 2}
        r.update(*lista, **dic)
        self.assertEqual(str(r), "[Rectangle] (9) 9/9 - 9/9")

#    ------------------------- Dictionary -----------------------

    def testdictionary(self):
        r = Rectangle(5, 6, 7, 8, 3)
        r1 = r.to_dictionary()
        pr = {'id': 3, 'width': 5, 'height': 6, 'x': 7, 'y': 8}
        for elem in pr:
            self.assertEqual(r1[elem], pr[elem])

    def testdictionary1(self):
        r = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(9)

#    ------------------------- no Arguments -------------------------------
    def testfargument1(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def testfargument2(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def testfargument3(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)


#    -------------------instance and inheritance ----------------------------

    def testinstandclass(self):
        r = Rectangle(4, 5)
        self.assertTrue(isinstance(r, Rectangle))
        self.assertTrue(isinstance(r, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(type(r) is Rectangle)

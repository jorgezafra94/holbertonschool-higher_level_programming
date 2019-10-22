#!/usr/bin/python3
"""
Unittest for Square Class
"""
from io import StringIO
from unittest.mock import patch
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):

    def testcreateelems(self):
        r = Square(1)
        r1 = Square(2, 5)
        r2 = Square(6, 8, 10)
        r3 = Square(1, 1, 1, 90)
        self.assertEqual(r.size, 1)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r2.size, 6)
        self.assertEqual(r2.x, 8)
        self.assertEqual(r2.y, 10)
        self.assertEqual(r3.size, 1)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 1)
        self.assertEqual(r3.id, 90)

    def testgetandset(self):
        r = Square(5)
        self.assertEqual(r.size, 5)
        r.size = 9
        self.assertEqual(r.size, 9)
        r = Square(1, 4)
        self.assertEqual(r.x, 4)
        r.x = 8
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 0)
        r.y = 8
        self.assertEqual(r.y, 8)
        r.id = 12
        self.assertEqual(r.id, 12)

#   ---------- tests for size -----------------------

    def testsize(self):
        with self.assertRaises(TypeError):
            r = Square("hola")

        with self.assertRaises(TypeError):
            r = Square([1, 2])

        with self.assertRaises(TypeError):
            r = Square((1, 2))

        with self.assertRaises(TypeError):
            r = Square({'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Square(0)

        with self.assertRaises(ValueError):
            r = Square(-8)

        with self.assertRaises(TypeError):
            r = Square(9.7)

#   ---------- tests for x -----------------------------
    def testx(self):
        with self.assertRaises(TypeError):
            r = Square(2, "hola")

        with self.assertRaises(TypeError):
            r = Square(1, [1, 2])

        with self.assertRaises(TypeError):
            r = Square(5, (1, 2))

        with self.assertRaises(TypeError):
            r = Square(6, {'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Square(6, -8)

        with self.assertRaises(TypeError):
            r = Square(2, 9.7)

    def testx1(self):
        r = Square(5, 0)
        self.assertEqual(r.x, 0)


#   ---------- tests for y -------------------------------

    def testy(self):
        with self.assertRaises(TypeError):
            r = Square(2, 5, "hola")

        with self.assertRaises(TypeError):
            r = Square(1, 5, [1, 2])

        with self.assertRaises(TypeError):
            r = Square(5, 6, (1, 2))

        with self.assertRaises(TypeError):
            r = Square(6, 7, {'a': 4, 'b': 8})

        with self.assertRaises(ValueError):
            r = Square(6, 9, -8)

        with self.assertRaises(TypeError):
            r = Square(8, 3, 9.7)

    def testy1(self):
        r = Square(5, 0, 0)
        self.assertEqual(r.y, 0)

#    ---------------------- id ----------------------------

    def testid(self):
        r = Square(3, 4, 5, 6)
        self.assertEqual(r.id, 6)
        r = Square(3, 4, 5, "6")
        self.assertEqual(r.id, "6")
        r = Square(3, 4, 5, {'id': 3})
        self.assertEqual(r.id, {'id': 3})
        r = Square(3, 4, 5, (1, 2))
        self.assertEqual(r.id, (1, 2))
        r = Square(3, 4, 5, [2, 4])
        self.assertEqual(r.id, [2, 4])

#    -----------  Area    ---------------------------------

    def testarea1(self):
        r = Square(5)
        self.assertEqual(r.area(), 25)

    def testarea2(self):
        r = Square(6)
        with self.assertRaises(TypeError):
            r.area(1)

#    ------------- Display ---------------------------------

    def testdisplay(self):
        with patch('sys.stdout', new=StringIO()) as salida:
            r = Square(2)
            r.display()
            st = "##\n##\n"
            self.assertEqual(salida.getvalue(), st)

        with patch('sys.stdout', new=StringIO()) as salida:
            r = Square(3, 2)
            r.display()
            st = "  ###\n  ###\n  ###\n"
            self.assertEqual(salida.getvalue(), st)

        with patch('sys.stdout', new=StringIO()) as salida:
            r = Square(2, 3, 2)
            r.display()
            st = "\n\n   ##\n   ##\n"
            self.assertEqual(salida.getvalue(), st)

    def testdisplay1(self):
        r = Square(1, 3)
        with self.assertRaises(TypeError):
            r.display(1)

#    -------------- __str__ ---------------------------------

    def tesstr(self):
        r = Square(2, 3, 4, 5)
        self.assertEqual(str(r), "[Square] (5) 3/4 - 2")

#    ----------------- Update -------------------------------

    def testupdate(self):
        r = Square(1, 1, 1, 1)
        self.assertEqual(str(r), "[Square] (1) 1/1 - 1")
        r.update(2, 2)
        self.assertEqual(str(r), "[Square] (2) 1/1 - 2")

        lista = [3, 4, 5]
        r.update(*lista)
        self.assertEqual(str(r), "[Square] (3) 5/1 - 4")

        lista = (1, 2, 4, 5)
        r.update(*lista)
        self.assertEqual(str(r), "[Square] (1) 4/5 - 2")

        lista = []
        r.update(*lista)
        self.assertEqual(str(r), "[Square] (1) 4/5 - 2")

        r.update()
        self.assertEqual(str(r), "[Square] (1) 4/5 - 2")

        di = {'x': 10, 'y': 20}
        r.update(**di)
        self.assertEqual(str(r), "[Square] (1) 10/20 - 2")

        di = {'id': 5, 'size': 5, 'x': 5, 'y': 5}
        r.update(**di)
        self.assertEqual(str(r), "[Square] (5) 5/5 - 5")

        lista = [9, 9, 9, 9]
        dic = {'id': 2, 'size': 2, 'x': 2, 'y': 2}
        r.update(*lista, **dic)
        self.assertEqual(str(r), "[Square] (9) 9/9 - 9")

#    ------------------------- Dictionary -----------------------

    def testdictionary(self):
        r = Square(6, 7, 8, 3)
        r1 = r.to_dictionary()
        pr = {'id': 3, 'size': 6, 'x': 7, 'y': 8}
        for elem in pr:
            self.assertEqual(r1[elem], pr[elem])

    def testdictionary1(self):
        r = Square(4, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(9)

#    ------------------------- no Arguments -------------------------------
    def testfargument1(self):
        with self.assertRaises(TypeError):
            r = Square()

    def testfargument2(self):
        with self.assertRaises(TypeError):
            r = Square(1, 2, 3, 4, 5)


#    -------------------instance and inheritance ----------------------------

    def testinstandclass(self):
        r = Square(4)
        self.assertTrue(isinstance(r, Square))
        self.assertTrue(isinstance(r, Rectangle))
        self.assertTrue(isinstance(r, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(type(r) is Square)
        self.assertTrue(hasattr(r, 'id'))
        self.assertTrue(hasattr(r, 'size'))
        self.assertTrue(hasattr(r, 'width'))
        self.assertTrue(hasattr(r, 'height'))
        self.assertTrue(hasattr(r, 'x'))
        self.assertTrue(hasattr(r, 'y'))

#!/usr/bin/python3
"""
class that inherits from Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    Args:
        * width: width of the rectangle
        * height: height of the rectangle
        * x: position in x
        * y: position in y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ return width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter width"""
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ return height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter height """
        if type(value) is int:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """ return x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter x"""
        if type(value) is int:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ return y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter y"""
        if type(value) is int:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """
        area: returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        display: print the rectangle
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            for p in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        __str__: print ecuation
        """
        args = (self.id, self.__x, self.__y, self.__width, self.__height)
        return("[Rectangle] ({}) {}/{} - {}/{}".format(*args))

    def update(self, *args, **kwargs):
        """
         update: update the values of the instance attributes
        """
        lista = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            cont = 0
            for arg in args:
                if cont < 5:
                    setattr(self, lista[cont], arg)
                    cont += 1
        else:
            for key, value in kwargs.items():
                for elem in lista:
                    if (elem == key):
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary: return the dictionary represntation of the instance
        """
        new = {}
        obj = self.__dict__
        lista = ['id', 'width', 'height', 'x', 'y']
        value = 0
        for cont in range(len(lista)):
            value = getattr(self, lista[cont])
            new[lista[cont]] = value
        return (new)

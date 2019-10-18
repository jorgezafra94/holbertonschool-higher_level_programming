#!/usr/bin/python3
"""
class that inherits from Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    Args:
        * width: instance attribute
        * height: instance attribute
        * x: instance attribute
        * y: instance attribute
    Functions:
        * area: returns the area of the rectangle
        * display: print the rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        args = (self.id, self.__x, self.__y, self.__width, self.__height)
        return("[Rectangle] ({}) {}/{} - {}/{}".format(*args))

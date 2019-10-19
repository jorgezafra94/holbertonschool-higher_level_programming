#!/usr/bin/python3
"""
class square that is an inheritance of Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Args:
        * size: size of the square
        * x: position
        * y: position
        * id: id of square
    methods:
        * __str__: print ecuation
        * update: updates the instance attributes
    """
    elem = 0

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__size = value
        else:
            raise TypeError("width must be an integer")

    def __str__(self):
        args = [self.id, self.x, self.y, self.size]
        return ("[Square] ({}) {}/{} - {}".format(*args))

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            cont = 0
            lista = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, lista[cont], arg)
                cont += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

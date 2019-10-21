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
        * dictionary: return the dictionary representation of the object
    """
    elem = 0

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        args = [self.id, self.x, self.y, self.size]
        return ("[Square] ({}) {}/{} - {}".format(*args))

    def update(self, *args, **kwargs):
        lista = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            cont = 0
            for arg in args:
                if cont < 4:
                    setattr(self, lista[cont], arg)
                    cont += 1
        else:
            for key, value in kwargs.items():
                for elem in lista:
                    if elem == key:
                        setattr(self, key, value)

    def to_dictionary(self):
        new = {}
        value = 0
        lista = ['id', 'size', 'x', 'y']
        for cont in range(len(lista)):
            value = getattr(self, lista[cont])
            new[lista[cont]] = value
        return (new)

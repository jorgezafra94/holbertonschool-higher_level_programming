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
    """
    elem = 0

    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ return width """
        return (self.width)

    @size.setter
    def size(self, size):
        """ setting size in width and height"""
        self.width = size
        self.height = size

    def __str__(self):
        """ python3 -m unittest tests/test_models/test_base.py"""
        args = [self.id, self.x, self.y, self.width]
        return ("[Square] ({}) {}/{} - {}".format(*args))

    def update(self, *args, **kwargs):
        """ update: updates the instance attributes"""
        lista = ['id', 'width', 'x', 'y']
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
                if key == 'size':
                    setattr(self, 'width', value)

    def to_dictionary(self):
        """ dictionary: return the dictionary representation of the object"""
        new = {}
        value = 0
        lista = ['id', 'size', 'x', 'y']
        for cont in range(len(lista)):
            if lista[cont] == 'size':
                value = getattr(self, 'width')
            else:
                value = getattr(self, lista[cont])
            new[lista[cont]] = value
        return (new)

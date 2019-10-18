#!/usr/bin/python3
"""
class square that is an inheritance of Rectangle class
"""


import models.rectangle from Rectangle


class Square(Rectangle):
    """
    Args:
        * size: size of the square
        * x: position
        * y: position
        * id: id of square
    methods:
        * __str__: print ecuation
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        args = [self.id, self.x, self.y, self.width]
        return ("[Square] ({}) {}/{} - {}".format(*args))

#!/usr/bin/python3
"""
main class of all the proyect

"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        if id is None increment the private class attribute __nb_objects
        else asign to self.id the value of id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id

#!/usr/bin/python3
import math


class MagicClass:

    """ Class that stores and manipulate the info of a circle
        get the area and circunference"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """ get the area depending of the radius of the circle"""
    def area(self):
        return ((self.__radius ** 2) * math.pi)

    """ get the circunference depending of the radius of the circle"""
    def circumference(self):
        return (2 * math.pi * self.__radius)

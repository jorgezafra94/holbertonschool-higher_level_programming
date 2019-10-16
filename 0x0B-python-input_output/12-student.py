#!/usr/bin/python3
"""
class Student
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is not list:
            return (self.__dict__)
        else:
            new = {}
            ob = self.__dict__
            for i in attrs:
                for ele in ob:
                    if (i == ele):
                        new[i] = ob[i]
            return (new)

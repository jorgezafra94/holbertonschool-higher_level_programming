#!/usr/bin/python3
"""

Class Mylist that is Ineritance form class list

"""


class MyList(list):
    """
    Args:
        * var: auxiliar variable in order to not affect the self value
        * self: variable that refers to the object itself
    """
    def print_sorted(self):
        var = []
        var = self.copy()
        var.sort()
        print(var)

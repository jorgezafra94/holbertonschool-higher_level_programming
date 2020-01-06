#!/usr/bin/python3
""" find the peak
"""


def find_peak(list_of_integers):
    """ function that get the peak from a list
    """
    if not list_of_integers:
        return (None)
    l = list_of_integers
    for i in range(len(l)):
        if (i == 0 or l[i] >= l[i + 1]) and (i == len(l) - 1 or l[i] >= l[i - 1]):
            return (l[i])

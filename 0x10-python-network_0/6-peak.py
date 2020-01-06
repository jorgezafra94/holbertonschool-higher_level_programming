#!/usr/bin/python3
""" find the peak
"""


def recursion(begin, last, l):
    """ search
    """
    mid = (begin + last)

    if (mid % 2 == 0):
        m = int(mid / 2)
    else:
        m = int((mid - 1) / 2)
    if (m == 0 or l[m] >= l[m - 1]) and (m == last - 1 or l[m] >= l[m + 1]):
        return (l[m])
    elif (m > 0 and l[m] < l[m - 1]):
        return (recursion(begin, m, l))
    elif (m < last - 1 and l[m] < l[m + 1]):
        return (recursion(m, last, l))
    else:
        return(None)


def find_peak(list_of_integers):
    """ function that get the peak from a list
    """
    if not list_of_integers:
        return (None)

    l = list_of_integers
    return (recursion(0, len(l), l))

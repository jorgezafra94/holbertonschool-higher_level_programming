#!/usr/bin/python3
""" find the peak
"""


def find_peak(list_of_integers):
    """ function that get the peak from a list
    """
    if not list_of_integers:
        return (None)
    if len(list_of_integers) < 3:
        aux = list_of_integers[0]
        for i in range(1, len(list_of_integers)):
            if list_of_integers[i] > aux:
                return(list_of_integers[i])
            else:
                return(aux)
    L = list_of_integers
    for i in range(1, len(L)):
        if (L[i] > L[i-1] and L[i] > L[i+1]):
            return(L[i])
    aux = L[0]
    for i in range(1, len(L)):
        if L[i] > aux:
            aux = L[i]
    return (aux)

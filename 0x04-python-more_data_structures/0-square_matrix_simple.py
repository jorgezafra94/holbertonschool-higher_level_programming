#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    else:
        new = []
        for element in matrix:
            newlist = list(map((lambda x: x * x), element))
            new.append(newlist)
        return (new)

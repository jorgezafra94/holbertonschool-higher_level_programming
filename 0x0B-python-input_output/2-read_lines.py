#!/usr/bin/python3
"""
print number of lines of a file
"""


def read_lines(filename="", nb_lines=0):
    sum = 0
    with open(filename) as fd:

        if nb_lines <= 0:
            for line in fd:
                print(line, end="")
        else:
            for i in range(nb_lines):
                print(fd.readline(), end="")

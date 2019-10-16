#!/usr/bin/python3
"""
print number of lines of a file
"""


def number_of_lines(filename=""):
    sum = 0
    with open(filename) as fd:
        for line in fd:
            sum += 1
    return (sum)

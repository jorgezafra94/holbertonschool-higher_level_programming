#!/usr/bin/python3
"""
Read and print the content of a file
"""


def read_file(filename=""):
    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")

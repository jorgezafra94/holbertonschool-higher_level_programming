#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            a, b = self.__size, self.__size
            for i in range(a):
                for j in range(b):
                    print("#", end="")
                print("")

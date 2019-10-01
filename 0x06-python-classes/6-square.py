#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            flag = 0
            for i in position:
                if not isinstance(i, int):
                    flag = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
                elif i < 0:
                    flag = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
                elif i > 2:
                    flag = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
            if flag == 0:
                self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        flag = 0
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in value:
                if not isinstance(i, int):
                    flag = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
                elif i < 0:
                    flag = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
                elif i > 2:
                    flag = 1
                    raise TypeError("position must be a tuple\
 of 2 positive integers")
            if flag == 0:
                self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            jump = self.__position[1]
            while (jump > 0):
                print()
                jump = jump - 1
            a, b = self.__size, self.__size
            for i in range(a):
                space = self.__position[0]
                for j in range(b):
                    while(space > 0):
                        print("", end=" ")
                        space = space - 1
                    print("#", end="")
                print("")

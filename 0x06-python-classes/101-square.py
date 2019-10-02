#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.size = size

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
        elif (len(value) != 2):
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
            if flag == 0:
                self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.size == 0):
            print()
        else:
            jump = self.position[1]
            while (jump > 0):
                print()
                jump = jump - 1
            a, b = self.size, self.size
            for i in range(a):
                space = self.position[0]
                for j in range(b):
                    while(space > 0):
                        print("", end=" ")
                        space = space - 1
                    print("#", end="")
                print("")

    def __str__(self):
        word = ""
        if (self.size == 0):
            return (word)
        else:
            jump = self.position[1]
            while (jump > 0):
                word = word + "\n"
                jump = jump - 1
            a, b = self.size, self.size
            for i in range(a):
                space = self.position[0]
                for j in range(b):
                    while(space > 0):
                        word += " "
                        space = space - 1
                    word += "#"
                if (i < self.size - 1):
                    word += "\n"
            return word

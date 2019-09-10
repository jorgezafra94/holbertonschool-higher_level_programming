#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is".format(number), end=" ")
if number < 0:
    number = number * (-1)
    last = (number % 10) * (-1)
    numer = number * (-1)
else:
    last = number % 10
if last > 5:
    print("{:d} and is greater than 5".format(last))
elif last < 6 and last != 0:
    print("{:d} and is less than 6 and not 0".format(last))
else:
    print("{:d} and is 0".format(last))

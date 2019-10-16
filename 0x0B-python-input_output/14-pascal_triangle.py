#!/usr/bin/python3


def pascal_triangle(n):
    result = []
    a = []
    if n <= 0:
        return (result)
    for i in range(n):
        if i == 0:
            a.append(1)
            result.append(a)
        elif i == 1:
            a = a + [1]
            result.append(a)
        else:
            new = []
            new.append(a[0])
            for j in range(len(a) - 1):
                sum = 0
                sum = a[j] + a[j + 1]
                new.append(sum)
            new.append(a[-1])
            a = new
            result.append(a)
    return (result)

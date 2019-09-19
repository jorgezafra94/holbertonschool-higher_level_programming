#!/usr/bin/python3
def roman_to_int(roman_string):
    c = 0
    result = 0
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    s = list(roman_string)
    for l in range(len(s)):
        arr = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        num = [1, 5, 10, 50, 100, 500, 1000]
        for i in range(len(arr)):
            if (s[l] == arr[i]):
                s[l] = num[i]
                break
    if len(s) == 1:
        return (s[0])
    else:
        for l in range(1, len(s)):
            if s[l - 1] >= s[l]:
                result = result + s[l - 1]
            else:
                result = result - s[l - 1]
        result = result + s[l]
        return result

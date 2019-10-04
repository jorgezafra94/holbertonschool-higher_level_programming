#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[1, 2, 5]], [[3, 4], [5, 6], [10, 10]]))
print(matrix_mul([[1, 4, 7], [2, 5, 8], [3, 6, 9]], [[1, -1, 2], [2, -1, 2], [3, -3, 0]]))
print(matrix_mul([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]]))
print(matrix_mul([[1, 5, 7]], [[3], [5], [8]]))

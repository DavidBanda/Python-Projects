import random
import re
import sys
import math
import os


# Complete the matrixRotation function below.
def matrixRotation(input_matrix, r):

    size = len(input_matrix) - 1

    # pruebas testing
    f = []
    l = []

    while size > 0:

        # obtienes el ultimo valor de la matriz siguiente
        # obtienes el primer valor de la matriz actual
        last = input_matrix[size][-1]
        first = input_matrix[size - 1][0]

        # elimino el ultimo valor de la matriz actual
        # elimino el primer valor de la matriz siguiente
        input_matrix[size].pop(-1)
        input_matrix[size - 1].pop(0)

        input_matrix[size].insert(0, first)

        if size == 1:
            input_matrix[size - 1].append(last)
        else:
            input_matrix[size - 1].insert(-1, last)



        # pruebas, testing
        l.append(last)
        f.append(first)

        size -= 1

    print(f)
    print(input_matrix)


if __name__ == '__main__':
    # mnr = input().rstrip().split()

    # m = 7
    #
    # n = 6

    r = 3

    matrix = [[1,   2,  3,  4,  5,  6],
              [7,   8,  9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30],
              [31, 32, 33, 34, 35, 36]]

    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)

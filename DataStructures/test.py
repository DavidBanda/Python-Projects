import math
import os
import random
import re
import sys

def matrixRotation(matrix, r):
    for i in range(m - 1):
        # obtenemos el primer elemento del actual array
        # y el ultimo del que sigue
        first = matrix[i][0]
        last = matrix[i + 1][-1]

        # añado al final del actual array la variable last
        # añado al index 1 del array siguiente la variable first
        matrix[i].append(last)
        matrix[i + 1].insert(1, first)

        # elimino el primer elemento del actual array,
        # el ultimo del segundo array
        matrix[i].pop(0)
        matrix[i + 1].pop(-1)

        # if i == m - 2:
        #     matrix[-1][0], matrix[-1][1] = matrix[-1][1], matrix[-1][0]

    print(matrix)

if __name__ == '__main__':
    # mnr = input().rstrip().split()

    m = 4

    n = 4

    r = 2

    matrix = [[1, 2, 3, 4], [12, 1, 2, 5], [11, 4, 3, 6],
              [10, 9, 8, 7]]

    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)



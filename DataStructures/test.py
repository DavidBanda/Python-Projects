import math
import os
import random
import re
import sys


def matrixRotation(matrix, r):
    size = len(matrix)
    for _ in range(r):
        rotate(matrix)
        if size >= 2:
            matrix2 = matrix[1:-1]
            for i in range(len(matrix2)):
                matrix2[i] = matrix2[i][1:-1]
            rotate(matrix2)

    if size > 2:
        for i in range(1, len(matrix2) + 1):
            for n in range(len(matrix2[0])):
                matrix[i][n + 1] = matrix2[i - 1][n]

        matrix[-2][1], matrix[-2][2] = matrix[-2][2], matrix[-2][1]

    for i in range(len(matrix)):
        st = ""
        for n in range(len(matrix[i])):
            # print(matrix[i][n])
            st += f'{matrix[i][n]} '
        st = st[:-1]
        print(st)

def rotate(input_matrix):
    for i in range(len(input_matrix) - 1):
        # obtenemos el primer elemento del actual array
        # y el ultimo del que sigue
        first = input_matrix[i][0]
        last = input_matrix[i + 1][-1]

        # añado al final del actual array la variable last
        # añado al index 1 del array siguiente la variable first
        input_matrix[i].append(last)
        input_matrix[i + 1].insert(1, first)

        # elimino el primer elemento del actual array,
        # el ultimo del segundo array
        input_matrix[i].pop(0)
        input_matrix[i + 1].pop(-1)

        if i == m - 2:
            input_matrix[-1][0], input_matrix[-1][1] = input_matrix[-1][1], input_matrix[-1][0]

    return input_matrix


if __name__ == '__main__':
    # mnr = input().rstrip().split()

    m = 4

    n = 4

    r = 2

    matrix = [[1, 2, 3, 4], [7, 8, 9, 10], [13, 14, 15, 16],
              [19, 20, 21, 22], [25, 26, 27, 28]]

    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)



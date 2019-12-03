import time


# Complete the matrixRotation function below.
def matrixRotation(input_matrix, r):
    for _ in range(r):
        rotate(input_matrix)
    for i in range(len(input_matrix)):
        print(" ".join(map(str, input_matrix[i])))


def rotate(input_matrix):

    size = len(input_matrix) - 1
    matrix2 = []
    # pruebas testing

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

        matrix2.append(input_matrix[size][1:-1])

        if size == 1:
            input_matrix[size - 1].append(last)
            matrix2 = matrix2[::-1]
            matrix2.pop()
        else:
            input_matrix[size - 1].insert(-1, last)

        size -= 1

    if len(input_matrix) == 2 or len(input_matrix) == 1 or len(input_matrix[0]) == 2:
        return input_matrix

    rotate(matrix2)

    for i in range(len(matrix2)):
        matrix2[i].insert(0, input_matrix[1:-1][i][0])
        matrix2[i].append(input_matrix[1:-1][i][-1])
    input_matrix[1:-1] = matrix2


if __name__ == '__main__':
    # mnr = input().rstrip().split()

    m = 6

    n = 5

    r = 1

    # matrix = [[1,   2,  3,  4,  5,  6],
    #           [7,   8,  9, 10, 11, 12],
    #           [13, 14, 15, 16, 17, 18],
    #           [19, 20, 21, 22, 23, 24],
    #           [25, 26, 27, 28, 29, 30],
    #           [31, 32, 33, 34, 35, 36]]

    # matrix = [[1,   2,  3,  4],
    #           [7,   8,  9, 10],
    #           [13, 14, 15, 16],
    #           [19, 20, 21, 22],
    #           [25, 26, 27, 28]]

    # matrix = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12],
    #           [13, 14, 15, 16]]

    # matrix = [[8, 9, 10, 19, 19, 20, 34],
    #           [14, 15, 34, 56, 98, 24, 46]]

    matrix = [[1, 2],
              [3, 4],
              [4, 5],
              [7, 8],
              [9, 10],
              [7, 9]]

    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))
    start = time.perf_counter()
    print(f'start: {start}')

    matrixRotation(matrix, r)

    finish = time.perf_counter()
    print(f'finish: {finish}')

# 2 3 4 5 11
# 1 9 10 16 17
# 7 8 21 22 23
# 13 14 15 28 29
# 19 20 26 27 35
# 25 31 32 33 34
# start: 69.151715372
# finish: 69.151978076
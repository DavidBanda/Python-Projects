import time


inputMatrix = [[1, 2],
                [3, 4],
                [5, 6],
                [7, 8]]
rotate = 8

inputMatrix2 = [[1, 2, 3, 4, 5, 6, 7, 8],
                [9, 10, 11, 12, 13, 14, 15, 16],
                [9, 10, 11, 12],
                [13, 14, 15, 16]]
rotate2 = 12

inputMatrix3 = [[9718805, 60013003, 5103628, 85388216, 21884498, 38021292, 73470430, 31785927],
                [69999937, 71783860, 10329789, 96382322, 71055337, 30247265, 96087879, 93754371],
                [79943507, 75398396, 38446081, 34699742, 1408833, 51189, 17741775, 53195748],
                [79354991, 26629304, 86523163, 67042516, 54688734, 54630910, 6967117, 90198864],
                [84146680, 27762534, 6331115, 5932542, 29446517, 15654690, 92837327, 91644840],
                [58623600, 69622764, 2218936, 58592832, 49558405, 17112485, 38615864, 32720798],
                [49469904, 5270000, 32589026, 56425665, 23544383, 90502426, 63729346, 35319547],
                [20888810, 97945481, 85669747, 88915819, 96642353, 42430633, 47265349, 89653362],
                [55349226, 10844931, 25289229, 90786953, 22590518, 54702481, 71197978, 50410021],
                [9392211, 31297360, 27353496, 56239301, 7071172, 61983443, 86544343, 43779176]]
rotate3 = 0

inputMatrix4 = [[9718805, 60013003, 5103628, 85388216, 21884498, 38021292, 73470430, 31785927],
                [69999937, 71783860, 10329789, 96382322, 71055337, 30247265, 96087879, 93754371],
                [79943507, 75398396, 38446081, 34699742, 1408833, 51189, 17741775, 53195748],
                [79354991, 26629304, 86523163, 67042516, 54688734, 54630910, 6967117, 90198864],
                [84146680, 27762534, 6331115, 5932542, 29446517, 15654690, 92837327, 91644840],
                [58623600, 69622764, 2218936, 58592832, 49558405, 17112485, 38615864, 32720798],
                [49469904, 5270000, 32589026, 56425665, 23544383, 90502426, 63729346, 35319547],
                [20888810, 97945481, 85669747, 88915819, 96642353, 42430633, 47265349, 89653362],
                [55349226, 10844931, 25289229, 90786953, 22590518, 54702481, 71197978, 50410021],
                [9392211, 31297360, 27353496, 56239301, 7071172, 61983443, 86544343, 43779176]]
rotate4 = 32


def arrayRotation(matrix, r):

    if r == 0:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col] = str(matrix[row][col])

    for _ in range(r):
        startRow, endRow = 0, len(matrix) - 1
        startCol, endCol = 0, len(matrix[0]) - 1
        while startRow <= endRow and startCol <= endCol:
            carry = matrix[startRow][startCol]
            for row in range(startRow + 1, endRow + 1):
                tempValue = matrix[row][startCol]
                matrix[row][startCol] = str(carry)
                carry = tempValue

            for col in range(startCol + 1, endCol + 1):
                tempValue = matrix[endRow][col]
                matrix[endRow][col] = str(carry)
                carry = tempValue

            for row in reversed(range(startRow, endRow)):
                tempValue = matrix[row][endCol]
                matrix[row][endCol] = str(carry)
                carry = tempValue

            for col in reversed(range(startCol, endCol)):
                tempValue = matrix[startRow][col]
                matrix[startRow][col] = str(carry)
                carry = tempValue

            startCol += 1
            startRow += 1
            endCol -= 1
            endRow -= 1

    for row in matrix:
        print(' '.join(row))


start = time.perf_counter()

arrayRotation(inputMatrix3, rotate3)
arrayRotation(inputMatrix4, rotate4)
print(inputMatrix3 == inputMatrix4)

finish = time.perf_counter()

# print(f'duration {finish - start}')









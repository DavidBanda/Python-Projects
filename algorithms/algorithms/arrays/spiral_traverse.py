input_array = [[1, 2, 3, 4],
               [12, 13, 14, 5],
               [11, 16, 15, 6],
               [10, 9, 8, 7]]

input_array2 = [[1, 2, 3, 4],
                [10, 11, 12, 5],
                [9, 8, 7, 6]]


def spiralTraverse(matrix):
    result = []
    startRow, endRow = 0, len(matrix) - 1
    startCol, endCol = 0, len(matrix[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(matrix[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(matrix[row][endCol])

        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            result.append(matrix[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            result.append(matrix[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1
    return result


print(spiralTraverse(input_array))





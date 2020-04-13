input_array = [[1, 2, 3, 4],
               [12, 13, 14, 5],
               [11, 16, 15, 6],
               [10, 9, 8, 7]]


def spiralTraverse(matrix):
    col = 0
    row = 0
    width = len(matrix[0]) - 1
    height = len(matrix) - 1
    arrayTraverse = []
    right = True
    down = False

    while width > 0 and height > 0:
        arrayTraverse.append(matrix[row][col])

        if right:
            col += 1
            if col == width:
                right = False
                down = True
        elif not right:
            pass

        if down:
            row += 1
            if row == height:
                right = False
        elif not down:
            pass

    return arrayTraverse


print(spiralTraverse(input_array))






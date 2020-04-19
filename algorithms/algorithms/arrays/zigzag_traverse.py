array = [[1, 3, 4, 10],
         [2, 5, 9, 11],
         [6, 8, 12, 15],
         [7, 13, 14, 16]]


def traverse_array(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    col, row = 0, 0
    is_down = True
    res = []

    while not is_out_of_boundaries(height, width, col, row):
        res.append(array[row][col])

        # Abajo
        if is_down:
            if col == 0 or row == height:
                is_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                col -= 1
                row += 1
        # Arriba
        else:
            if row == 0 or col == width:
                is_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                col += 1
                row -= 1

    return res


def is_out_of_boundaries(height, width, col, row):
    return col < 0 or col > width or row < 0 or row > height


print(traverse_array(array))




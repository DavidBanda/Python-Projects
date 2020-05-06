input_array = [2, 1, 2, 2, 2, 3, 4, 2]
to_move = 2


def move_element_to_end(array, toMove):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx < rightIdx:
        while leftIdx < rightIdx and array[rightIdx] == toMove:
            rightIdx -= 1

        if array[leftIdx] == toMove:
            array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
        leftIdx += 1

    return array


print(move_element_to_end(input_array, to_move))








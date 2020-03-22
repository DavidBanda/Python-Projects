input_array = [2, 1, 2, 2, 2, 3, 4, 2]
to_move = 2

input_array2 = [3, 3, 3, 3, 3]
to_move2 = 3

input_array3 = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
to_move3 = 5


def move_element_to_end(array, to_move):
    left = 0
    right = len(array) - 1

    while left < right:
        while left < right and array[right] == to_move:
            right -= 1

        if array[left] == to_move:
            array[left], array[right] = array[right], array[left]

        left += 1

    return array


print(move_element_to_end(input_array3, to_move3))








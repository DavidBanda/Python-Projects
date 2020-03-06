array = [8, 5, 2, 9, 5, 6, 3]


def find_three_largest_numbers(array):

    for _ in range(3):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array[-3::]


print(find_three_largest_numbers(array))


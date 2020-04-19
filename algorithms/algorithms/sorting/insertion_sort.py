input_array = [8, 5, 2, 9, 5, 6, 3]


def insertionSort(array):

    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array


print(insertionSort(input_array))








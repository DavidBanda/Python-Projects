array = [8, 5, 2, 9, 5, 6, 3]


def bubble_sort(array):

    for i in range(1, len(array)):
        for j in range(len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(bubble_sort(array))


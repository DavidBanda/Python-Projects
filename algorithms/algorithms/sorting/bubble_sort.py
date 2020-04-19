array = [8, 5, 2, 9, 5, 6, 3]


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

print(bubble_sort(array))


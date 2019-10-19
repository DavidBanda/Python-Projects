from math import log2, ceil

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#     [0, 1, 2, 3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14]


def binary_search1(input_array, value):
    low = 0
    high = len(input_array) - 1
    loop = ceil(log2(high))
    
    if isinstance(loop, int):
        loop += 1

    for i in range(loop):

        mid = int((low + high) / 2)

        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search2(input_array, value):
    low = 0
    high = len(input_array) - 1

    while low <= high:

        mid = int((low + high) / 2)

        if input_array[mid] == value:
            return mid
        elif input_array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(binary_search2(arr, 15))

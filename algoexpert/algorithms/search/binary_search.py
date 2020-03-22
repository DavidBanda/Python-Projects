input_array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
digit = 72


def binarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if target < array[middle]:
            right = middle - 1
        elif target > array[middle]:
            left = middle + 1
        else:
            return middle

    return -1


print(binarySearch(input_array, digit))



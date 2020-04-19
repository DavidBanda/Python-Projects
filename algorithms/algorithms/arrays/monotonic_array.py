# decreasing
input_array = [-1, -5, -10, -1100, -1100, -1100, -1101, -1102, -9001]

# increasing
input_array2 = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11]


def isMonotonic(array):
    isIncreasing = True
    isDecreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isIncreasing = False
        if array[i] > array[i - 1]:
            isDecreasing = False
    return isDecreasing or isIncreasing


print(isMonotonic(input_array))




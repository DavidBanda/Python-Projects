input_array = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]


def threeRange(array):
    left = 0
    middle = 1
    right = 2
    rangeResult = ''
    while right < len(array):
        if array[left] + 1 == array[middle] and array[middle] + 1 == array[right]:
            while right < len(array):
                if array[middle] + 1 == array[right]:
                    middle += 1
                    right += 1
                else:
                    break
            rangeResult += f'{array[left]}-{array[right - 1]},'
            left = right
            middle = left + 1
            right = middle + 1
        else:
            rangeResult += f'{array[left]},'
            left += 1
            middle += 1
            right += 1

    return rangeResult[:-1]


print(threeRange(input_array))






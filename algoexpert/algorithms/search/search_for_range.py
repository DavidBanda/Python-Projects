input_array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
input_target = 73


def searchForRange(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        pivot = (left + right) // 2
        if target < array[pivot]:
            right = pivot - 1
        elif target > array[pivot]:
            left = pivot + 1
        else:
            left = pivot - 1
            right = pivot + 1
            while left > 0 and target == array[left]:
                left -= 1
            while right < len(array) and target == array[right]:
                right += 1
            return [left + 1, right - 1]
    return [-1, -1]


print(searchForRange(input_array, input_target))

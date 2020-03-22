input_array = [7, 6, 4, -1, 1, 2]
digit = 16

input_array2 = [1, 2, 3, 4, 5, 6, 7]
digit2 = 10


def fourNumberSum(array, targetSum):
    array.sort()
    quadruplets = []

    for i in range(len(array) - 3):
        left = i + 2
        right = len(array) - 1

        while left < right:
            current_sum = array[i] + array[i + 1] + array[left] + array[right]
            if current_sum == targetSum:
                quadruplets.append([array[i], array[i + 1], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1

    return quadruplets


print(fourNumberSum(input_array2, digit2))

input_array = [12, 3, 1, 2, -6, 5, -8, 6]
digit = 0


def three_number_sum(array, targetSum):
    array.sort()
    res = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == targetSum:
                res.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < targetSum:
                left += 1
            elif current_sum > targetSum:
                right -= 1

    return res


print(three_number_sum(input_array, digit))

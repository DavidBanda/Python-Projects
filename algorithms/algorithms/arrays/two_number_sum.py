# Write a function that takes in a non-empty array of distinct integers and
# an integer representing a target sum. If any two numbers in the input array
# sum up to the target sum, the function should return them in an array.
# If no two numbers sum up to the target sum, the function should return an
# empty array. Assume that there will be at most one pair of numbers summing
# up to the target sum.

# Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
# Sample output: [-1, 11]

example_array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
example_digit = 164

example_array2 = [3, 5, -4, 8, 11, 1, -1, 6]
example_digit2 = 10


# O(n^2) T | O(1) S
def two_number_sum_n2(array, digit):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == digit:
                return [array[i], array[j]]

    return []


# print(two_number_sum_n2(example_array2, example_digit2))


# O(n) ST
def two_number_sum_n(array, digit):
    hash_table = {}

    for num in array:
        res = digit - num
        if res in hash_table:
            return [res, num]
        else:
            hash_table[num] = True

    return []


# print(two_number_sum_n(example_array2, example_digit2))


# O(nlogn) T | O(1) S
def two_number_sum_nlogn(array, digit):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] + array[right] == digit:
            return [array[left], array[right]]
        elif array[left] + array[right] < digit:
            left += 1
        elif array[left] + array[right] > digit:
            right -= 1

    return []


print(two_number_sum_nlogn(example_array2, example_digit2))



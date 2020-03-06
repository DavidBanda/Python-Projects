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


# o(n^2) S
def two_number_sum_n2(array, digit):

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if digit == array[i] + array[j]:
                return [array[i], array[j]]

    return []


# print(two_number_sum_n2(example_array, example_digit))


# o(n) - ST
def two_number_sum_n(array, digit):

    hash_table = {}
    for num in array:
        other_digit = digit - num
        if other_digit in hash_table:
            return [num, other_digit]
        else:
            hash_table[num] = True
    return []


# print(two_number_sum_n(example_array2, example_digit2))


# example_array2 = [3, 5, -4, 8, 11, 1, -1, 6]
# example_digit2 = 10
# example_array2 sorted [-4, -1, 1, 3, 5, 6, 8, 11]
# o(n_log_n)
def two_number_sum_n_log_n(array, digit):

    array.sort()
    left = 0
    right = len(array) - 1
    print(array)

    while left < right:
        sum = array[left] + array[right]
        if sum == digit:
            return [array[left], array[right]]
        elif sum < digit:
            left += 1
        elif sum > digit:
            right -= 1
    return []


print(two_number_sum_n_log_n(example_array2, example_digit2))

input_array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]


def largest_range(array):
    num_store = {}
    longest_range = 0
    result_range = []

    for i in array:
        num_store[i] = True

    for i in array:

        current_range = 0
        first_value = i
        while i in num_store:
            current_range += 1
            i += 1

        if current_range > longest_range:
            longest_range = current_range
            result_range = [first_value, i - 1]

    return result_range


print(largest_range(input_array))




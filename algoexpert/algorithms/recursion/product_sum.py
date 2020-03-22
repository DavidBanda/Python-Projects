input_array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]


def productSum(array, multiplier=1):
    sum = 0

    for i in array:
        if type(i) is int:
            sum += i
        else:
            sum += productSum(i, multiplier + 1)

    return multiplier * sum


print(productSum(input_array))





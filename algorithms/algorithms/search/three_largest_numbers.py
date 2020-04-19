# array = [8, 5, 2, 9, 5, 6, 3]
#
#
# def find_three_largest_numbers(array):
#
#     for _ in range(3):
#         for i in range(len(array) - 1):
#             if array[i] > array[i + 1]:
#                 array[i], array[i + 1] = array[i + 1], array[i]
#     return array[-3::]
#
#
# print(find_three_largest_numbers(array))


import random
import time

# input_array = [random.randint(-100, 100) for _ in range(1000000)]
input_array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

start = time.perf_counter()
print(f'start: {start}')


def findThreeLargestNumbers(array):
    threeLargestNumbers = [None, None, None]
    for num in array:
        if threeLargestNumbers[2] is None or num > threeLargestNumbers[2]:
            num = changeNumber(threeLargestNumbers, num, 2)
        if threeLargestNumbers[1] is None or num > threeLargestNumbers[1]:
            num = changeNumber(threeLargestNumbers, num, 1)
        if threeLargestNumbers[0] is None or num > threeLargestNumbers[0]:
            changeNumber(threeLargestNumbers, num, 0)
    return threeLargestNumbers


def changeNumber(threeLargestNumbers, num, pos):
    newNum = threeLargestNumbers[pos]
    threeLargestNumbers[pos] = num
    return newNum


print(findThreeLargestNumbers(input_array))
finish = time.perf_counter()
print(f'finish: {finish}')

print(f'Finished in {round(finish-start, 2)} second(s)')







arrayOne = [10, 8, 5, 15, 2, 12, 11, 94, 81]
arrayTwo = [10, 15, 8, 12, 94, 81, 5, 2, 11]


def sameBsts(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne)
    print(arrayTwo)
    print(arrayOne == arrayTwo)


print(sameBsts(arrayOne, arrayTwo))












inputArrayOne = [-1, 5, 10, 20, 28, 3]
inputArrayTwo = [26, 134, 135, 15, 17]


def smallest_difference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne)
    print(arrayTwo)
    currentValue = 0
    closestValue = float('inf')
    pairNumbers = []
    arrayOneIdx = 0
    arrayTwoIdx = 0
    while arrayOneIdx < len(arrayOne) and arrayTwoIdx < len(arrayTwo):
        firstValue = arrayOne[arrayOneIdx]
        secondValue = arrayTwo[arrayTwoIdx]

        if firstValue < secondValue:
            currentValue = secondValue - firstValue
            arrayOneIdx += 1
        elif secondValue < firstValue:
            currentValue = firstValue - secondValue
            arrayTwoIdx += 1
        else:
            return [firstValue, secondValue]

        if currentValue < closestValue:
            closestValue = currentValue
            pairNumbers = [firstValue, secondValue]

    return pairNumbers


print(smallest_difference(inputArrayOne, inputArrayTwo))







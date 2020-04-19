input_array = [7, 6, 4, -1, 1, 2]
digit = 16

input_array2 = [1, 2, 3, 4, 5, 6, 7]
digit2 = 10


def fourNumberSum(array, targetSum):
    allPairs = {}
    quadruplets = []
    for i in range(1, len(array)):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairs:
                for pair in allPairs[difference]:
                    quadruplets.append(pair + [array[i], array[j]])
        for k in range(0, i):
            currentSum = array[i] + array[k]
            if currentSum in allPairs:
                allPairs[currentSum].append([array[k], array[i]])
            else:
                allPairs[currentSum] = [[array[k], array[i]]]
    return quadruplets


print(fourNumberSum(input_array, digit))

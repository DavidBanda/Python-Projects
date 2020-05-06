input_array = [12, 3, 1, 2, -6, 5, -8, 6]
digit = 0


def three_number_sum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        leftIdx = i + 1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            sum = array[i] + array[leftIdx] + array[rightIdx]
            if sum < targetSum:
                leftIdx += 1
            elif sum > targetSum:
                rightIdx -= 1
            else:
                triplets.append([array[i], array[leftIdx], array[rightIdx]])
                leftIdx += 1
                rightIdx -= 1
    return triplets


print(three_number_sum(input_array, digit))

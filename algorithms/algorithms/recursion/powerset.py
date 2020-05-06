inputArray = [1, 2, 3]


def powerset(array):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            current = subsets[i]
            subsets.append(current + [element])
    return subsets


print(powerset(inputArray))













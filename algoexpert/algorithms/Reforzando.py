array = [1, 2, 3]

# O(n*n!) Time | O(n*n!)
def getPermutations(array):
    permutations = []
    seekPermutations(0, array, permutations)
    return permutations


def seekPermutations(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(i, j, array)
            seekPermutations(i + 1, array, permutations)
            swap(i, j, array)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


print(getPermutations(array))






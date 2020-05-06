sequence = [1, 3, 2]


def almostIncreasingSequence(sequence):
    remove = 0
    for i in range(1, len(sequence)):

        if sequence[i] > sequence[i - 1]:
            continue

        remove += 1

    return False if remove > 1 else True


print(almostIncreasingSequence(sequence))





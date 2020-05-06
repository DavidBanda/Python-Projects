n = 4


def getQueensPosition(n):
    queensPosition = []
    depthFirstSearch([], [], [], queensPosition, n)
    return queensPosition


def depthFirstSearch(queens, slopeDown, slopeUp, queensPosition, n):

    row = len(queens)

    if row == n:
        queens = [[0 if x != digit else 1 for x in range(n)] for digit in queens]
        queensPosition.append(queens[:])

    for col in range(n):
        if col in queens or row - col in slopeDown or row + col in slopeUp:
            continue

        depthFirstSearch(queens + [col],
                         slopeDown + [row - col],
                         slopeUp + [row + col],
                         queensPosition, n)


[print(f'{[print(row) for row in element]}') for element in getQueensPosition(n)]




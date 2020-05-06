def solveNQueens(n):
    queensPosition = []
    DFS([], [], [], queensPosition, n)
    return queensPosition


def DFS(queens, xy_intersect_down, xy_intersect_up, queensPosition, n):
        row = len(queens)

        if row == n:
            queens = ['.' * i + 'Q' + '.' * (n - 1 - i) for i in queens]
            queensPosition.append(queens)
            return

        for col in range(n):

            if col in queens or row - col in xy_intersect_down or row + col in xy_intersect_up:
                continue

            DFS(queens + [col],
                xy_intersect_down + [row - col],
                xy_intersect_up + [row + col],
                queensPosition, n)

#      y2 - y1
# m = ---------  (1, 45º, /), (-1, 145º, \)
#      x2 - x1

# y = mx + b |  y - x = b, y + x = b


[print([print(pos) for pos in row], "") for row in solveNQueens(4)]


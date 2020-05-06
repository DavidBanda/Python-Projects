sudoku = [["5", "3", ".",   ".", "7", ".",   ".", ".", "."],
          ["6", ".", ".",   "1", "9", "5",   ".", ".", "."],
          [".", "9", "8",   ".", ".", ".",   ".", "6", "."],

          ["8", ".", ".",   ".", "6", ".",   ".", ".", "3"],
          ["4", ".", ".",   "8", ".", "3",   ".", ".", "1"],
          ["7", ".", ".",   ".", "2", ".",   ".", ".", "6"],

          [".", "6", ".",   ".", ".", ".",   "2", "8", "."],
          [".", ".", ".",   "4", "1", "9",   ".", ".", "5"],
          [".", ".", ".",   ".", "8", ".",   ".", "7", "9"]]


def solveSudoku(sudoku):
    solve(sudoku)
    return sudoku


def solve(sudoku):
    for row in range(len(sudoku)):
        for col in range(len(sudoku[0])):
            if sudoku[row][col] == '.':
                for num in range(1, 10):
                    num = str(num)
                    if isValid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve(sudoku):
                            return True
                        sudoku[row][col] = '.'
                return False
    return True


def isValid(sudoku, row, col, num):
    for r in range(len(sudoku)):
        if sudoku[r][col] == num:
            return False
    for c in range(len(sudoku[0])):
        if sudoku[row][c] == num:
            return False
    for r in range((row//3)*3, (row//3 + 1)*3):
        for c in range((col//3)*3, (col//3 + 1)*3):
            if sudoku[r][c] == num:
                return False
    return True


[print(row) for row in solveSudoku(sudoku)]




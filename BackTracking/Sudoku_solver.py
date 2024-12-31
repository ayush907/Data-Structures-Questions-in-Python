# function for ckecking the position is safe or not 
def is_safe(sudoku, row, col, digit):
    # checking for row
    for i in range(9):
        if sudoku[i][col] == digit:
            return False
        
    # checking for column
    for j in range(9):
        if sudoku[row][j] == digit:
            return False
        
    # checking for mini grid
    sr = (row // 3) * 3
    sc = (col // 3) * 3

    for i in range(sr,sr+3):
        for j in range(sc, sc+3):
            if sudoku[i][j] == digit:
                return False
            
    return True



# the sudoku solver function
def sudoku_solver(sudoku, row, col):
    # base case
    if row == 9 and col == 0:    # boundary cross check
        return True


    # recursion 
    next_row = row
    next_col = col + 1
    if col+1 == 9: 
        next_row = row + 1
        next_col = 0

    if sudoku[row][col] != 0:
        return sudoku_solver(sudoku, next_row, next_col)

    for digit in range(10):
        if is_safe(sudoku, row, col, digit):
            sudoku[row][col] = digit
            if sudoku_solver(sudoku, next_row, next_col):
                return True
            sudoku[row][col] = 0

    return False


# function for printing the sudoku
def print_sudoku(sudoku):
    rows = len(sudoku)
    cols = len(sudoku[0])
    for i in range(rows):
        for j in range(cols):
            print(sudoku[i][j], end=" ")
        print()


sudoku = [
    [0,0,8,0,0,0,0,0,0],
    [4,9,0,1,5,7,0,0,2],
    [0,0,3,0,0,4,1,9,0],
    [1,8,5,0,6,0,0,2,0],
    [0,0,0,0,2,0,0,6,0],
    [9,6,0,4,0,5,3,0,0],
    [0,3,0,0,7,2,0,0,4],
    [0,4,9,0,3,0,0,5,7],
    [8,2,7,0,0,9,0,1,3]
]

sudoku_solver(sudoku, 0, 0)

print_sudoku(sudoku)



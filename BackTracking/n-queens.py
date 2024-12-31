# function for checking the position is safe or not for queen
def is_safe(board, row, col):

    # vertically up check 
    for i in range(row-1, -1, -1):
        if(board[i][col] == "Q"):
            return False
        
    # diagonally left up check 
    for i, j in zip(range(row-1,-1, -1), range(col-1, -1, -1)):
            if board[i][j] == "Q":
                return False
            
    # diagonally right up check
    for i,j in zip(range(row-1, -1, -1), range(col+1, len(board))):
            if board[i][j] == "Q":
                return False
            
    return True
        

# function for n-queens
def n_queens(board, row):
    # base case
    if row == len(board):
        print_board(board)
        print("----------------------------")
        return
    
    for j in range(len(board[0])):
        if is_safe(board, row, j):    #agar position safe hai toh he queen place karo
            board[row][j] = "Q"
            n_queens(board, row + 1)
            board[row][j] = "."

# board print karwaane ka function
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

# board initialize karne ka function
def initialize_board(n):
    arr = [["." for i in range(n)] for i in range(n)]
    return arr


board = initialize_board(5)

n_queens(board, 0)



# find the total number of ways to reach from (0,0) to (n-1, m-1) in a (n x m) Grid.

def grid_ways(i, j, n, m):
    # base case
    if i == n-1 and j == m-1:  # condition for last cell.
        return 1
    elif(i == n or j == m):    # condition for boundary cross.
        return 0
    
    w1 = grid_ways(i , j+1, n, m)
    w2 = grid_ways(i+1 , j, n, m)

    return w1 + w2

n, m = 3, 3
print(grid_ways(0, 0, n, m))
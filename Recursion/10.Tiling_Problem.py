# Tiling problem : given a (2 X n) and tiles of size (2 X 1), we have to find the total no. of ways to tile the given board using the (2 X 1) tiles.

def tilingProblem(n):
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    fnm1 = tilingProblem(n - 1)   # vertical filling ke baad (n - 1) tiles pe recursion laga do.
    fnm2 = tilingProblem(n - 2)   # horizontal filling ke baad (n - 2) tiles pe recursion laga do.

    total_ways = fnm1 + fnm2

    return total_ways


print(tilingProblem(5))

    
    


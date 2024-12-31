
# Print Numbers in Increasing Order
# increasing order mai print karaane ke 2 variations hai 

# 1. first variation.
def printIncreasing(num):
    # base case
    if num == 0:
        return
    
    printIncreasing(num - 1)
    print(num)

# ess variation mai hame jis number tak increasing order mai print karwaana hai vo number input dena hai. 
printIncreasing(10)


print("----------X-------------X-------------X-----------")

# 2. second variation
# ess variation mai hamko jis number tak number print karaane hai usko (base case) banaana hai.
def printIncreasingTwo(num):
    if num == 10: 
        print(num)
        return
    
    print(num)
    printIncreasingTwo(num + 1)

printIncreasingTwo(1)
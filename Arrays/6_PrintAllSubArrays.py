# function for printing all the subarrays of an array

def printSubArrays(arr):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            for k in range(i,j+1):    # final loop (i to j) ke beech mai loop chalega jo elements print karega
                print(arr[k], end=" ")
            print()
        print()


arr = [1,2,3,4,5]
printSubArrays(arr)
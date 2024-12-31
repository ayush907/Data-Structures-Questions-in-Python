# python code to print the pairs of an array 
def pairsInArray(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1, n):
            print(f"({arr[i]}, {arr[j]})", end = " ")
        print()


arr = [1,2,3,4,5]
pairsInArray(arr)

# function to check if the array is sorted or not

def checkSorted(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                return False
            
    return True


arr = [1, 2, 3, 4, 5, 8, 6]

print(checkSorted(arr))
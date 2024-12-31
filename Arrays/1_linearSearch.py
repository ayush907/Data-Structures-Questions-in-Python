# function for linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key: 
            return i 
        
    return - 1

arr = [2,3,4,1,6,5]
key = 6
print(linear_search(arr, key))


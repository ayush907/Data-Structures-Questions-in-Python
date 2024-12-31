# iterativ approach of binary search

def binary_search(arr, key):
    low = 0           #calculate low 
    high = len(arr) - 1     #calculate high

    while low <= high:

        mid = (low + high) // 2  #mid calculate karo.

        if(arr[mid] == key):
            return mid  # return the mid because mid is the index of the key.
        
        elif(key > arr[mid]): 
            low = mid + 1

        else: 
            high = mid - 1

    return -1   # if the element is not found in the array return -1.

arr = [1,3,5,7,9]

print(binary_search(arr, 10))
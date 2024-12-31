# binarySearch using recursion 
def binarySearch(arr, low, high, key):

    if(low <= high):

        mid = (low + high) // 2

        if(arr[mid] == key):
            return mid
        
        elif(key > arr[mid]):
            return binarySearch(arr, mid + 1, high, key)
        
        else: 
            return binarySearch(arr, low, mid - 1, key)
        
    return - 1

arr = [1,2,5,7,9]
low = 0
high = len(arr) - 1
key = int(input("enter the element to search: "))
print(binarySearch(arr, low, high, key))



# checking if the array is sorted using recursion 
def is_sorted(arr, idx):
    if idx == len(arr)-1:
        return True
    
    if arr[idx] > arr[idx + 1]:
        return False
    
    return is_sorted(arr, idx + 1)


arr = [1,2,3,4,5,6]
print(is_sorted(arr, 0))
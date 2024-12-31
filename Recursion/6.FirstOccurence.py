# Recursive function to get(Index) the first occurence of an element in the array
def first_occurence(arr,idx, key):
    if idx == len(arr):
        return -1
    
    if arr[idx] == key:
        return idx
    
    return first_occurence(arr, idx+1, key)

arr = [3,2,5,6,1]
print(first_occurence(arr,0,10))
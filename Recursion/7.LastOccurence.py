# Recursive Function to get(Index) the last occurence of the element in the array

def last_occurence(arr, idx, key):
    if idx == len(arr):
        return -1
    
    if arr[idx] == key:
        next_idx = last_occurence(arr, idx+1, key)   # agar key mili  toh next recursion uske baad lagaayenge.
        if next_idx != -1:
            return next_idx
        return idx
    
    return last_occurence(arr, idx+1, key)

arr = [2,3,1,5,6,7]
print(last_occurence(arr,0,2))
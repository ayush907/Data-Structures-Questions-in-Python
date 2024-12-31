# function for reversing an array
def reverseArray(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]

        start = start + 1
        end = end - 1
        # print(arr) 
    return arr

arr = [1,2,3,4,5]
print(reverseArray(arr))


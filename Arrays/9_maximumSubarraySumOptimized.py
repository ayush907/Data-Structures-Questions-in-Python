# prefix sum ka array create karne ke liye function
def prefixSumArray(arr):
    prefixSumArr = [0] * len(arr)
    prefixSumArr[0] = arr[0]
    for i in range(1,len(prefixSumArr)):
        prefixSumArr[i] = prefixSumArr[i-1] + arr[i]

    return prefixSumArr


def maxSubarraySumOptimized(arr):
    prefix = prefixSumArray(arr)
    max_sum = 0
    curr_sum = 0
    for i in range(len(arr)):
        start = i
        for j in range(i,len(arr)):
            end = j
            curr_sum = prefix[end] if start == 0 else prefix[end] - prefix[start - 1]

            if curr_sum > max_sum:
                max_sum = curr_sum
            print("tracking the max_sum",max_sum)
    return max_sum


arr = [1,2,3,4,5]

print(maxSubarraySumOptimized(arr))

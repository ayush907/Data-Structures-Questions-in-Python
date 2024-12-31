# function to print maximum subarray sum

def maximumSubarraySum(arr):
    max_sum = 0
    curr_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            curr_sum = 0    # har ek subarray ka sum print karwaa ke curr_sum ko again 0 sut karenge.
            for k in range(i, j+1):
                curr_sum = curr_sum + arr[k]
            print("current sum is ",curr_sum)    # har ek subarray ke liye curr_sum calculate karke usko print karwaayenge
            if curr_sum > max_sum: 
                max_sum = curr_sum
            print("abhi tak ka maxsum ", max_sum)

    return max_sum    #last mai max_sum return kar denge


# def maximumSubarraySum(arr):
#     max_sum = 0
#     curr_sum = 0
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             curr_sum = 0    # har ek subarray ka sum print karwaa ke curr_sum ko again 0 sut karenge.
#             for k in range(i, j+1):
#                 curr_sum = curr_sum + arr[k]
#             if curr_sum > max_sum: 
#                 max_sum = curr_sum
#             print("current sum is ",curr_sum)    # har ek subarray ke liye curr_sum calculate karke usko print karwaayenge
#     print("abhi tak ka maxsum ", max_sum)

#     return max_sum    #last mai max_sum return kar denge


arr = [1,2,3,4,5]
print(maximumSubarraySum(arr))

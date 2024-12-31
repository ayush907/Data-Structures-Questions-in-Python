# program to print x to the power n

def power_function(x, n):
    if n == 0: 
        return 1
    # elif n == 1: 
    #     return x
    
    return x * power_function(x, n-1)

print(power_function(2,3))
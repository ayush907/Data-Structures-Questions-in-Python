# optimized recursive power function

def power_optimized(x, n):
    if n == 0:     # Base case
        return 1
    
    half_power = power_optimized(x, int(n/2))  # memoize ka liya power function ko
    half_power_sq = half_power * half_power
    
    if n % 2 != 0:
        return x * half_power_sq
    
    return half_power_sq


print(power_optimized(2,2))




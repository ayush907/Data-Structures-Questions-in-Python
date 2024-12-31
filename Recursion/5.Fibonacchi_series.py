# function to print the Nth fibonaacchi number
def Fibonacchi(n):
    if n == 1:
        return 0
    
    elif n == 2: 
        return 1
    
    return Fibonacchi(n - 1) + Fibonacchi(n - 2)

# yaha pe ham user se imput lekar fibonnacchi series print karenge
x = int(input("konsi position tak ki fibonacchi series chahiye: "))
for i in range(1, x+1):
    print(Fibonacchi(i), end = " ")
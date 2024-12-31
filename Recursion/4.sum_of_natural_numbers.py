# recursive function to print the sum of n natural numbers

# first variation
def sum_of_n_first(num):
    # base case
    if num <= 0:
        return 0
    
    return num + sum_of_n_first(num-1)

# print(sum_of_n_first(5))    

    

# second variation
def sum_of_n_second(num, sum):
    # base case
    if num < 0:
        print(sum)
        return
    # sum = sum + num
    # num = num - 1
    # print(sum)  # ess function mai ham sum ki value ka track bhi rakh sakte hai 
    sum_of_n_second(num - 1, sum + num)

sum_of_n_second(5,0)


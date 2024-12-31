# 1. print numbers in Decreaing Order

def PrintDecreasing(num):
    # Base case
    if num == 0:
        return

    print(num)     # pehle num ko print karo  
    PrintDecreasing(num-1)     # firr agle level ke liye call lagaao

PrintDecreasing(10)



    


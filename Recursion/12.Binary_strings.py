# Recursive function to print all the Binary Strings without the consecutive ones

def BinaryStrings(n, lastPlace, new_st):
    # base case
    if n == 0:
        print(new_st)
        return
    
    # doo  dividing recursive calls lagengi (ek call conditional hogi).
    BinaryStrings(n-1, 0, new_st + "0")
    if lastPlace == 0:
        BinaryStrings(n-1, 1, new_st + "1")

BinaryStrings(3, 0, "")



# # Recursive function to print all the Binary Strings without consecutive ones

# def BinaryStrings(n, lastPlace, new_st):
#     # Base case: Jab n 0 ho jaye, matlab binary string complete ho gayi hai, toh current string print kar do
#     if n == 0:
#         print(new_st)
#         return
    
#     # Recursive case: Pehle "0" add karo current string mein, aur n ko 1 reduce kar do
#     # Ye step har case mein chalega, kyunki "0" se consecutive 1 nahi bante
#     BinaryStrings(n-1, 0, new_st + "0")
    
#     # "1" tabhi add karo jab last character "0" ho, matlab consecutive "1"s nahi hone chahiye
#     if lastPlace == 0:
#         BinaryStrings(n-1, 1, new_st + "1")

# # Function ko call karte hain, jisme n = 3 hai, starting "lastPlace" 0 hai aur empty string se start karte hain
# BinaryStrings(3, 0, "")

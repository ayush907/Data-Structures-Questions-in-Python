# string mai se duplicate remove karne ka recursive program 

def remove_duplicate(st, idx, newstr, seen_arr):
    # base case
    if idx == len(st):
        print(newstr)
        return
    
    # current index calculate karo
    curr_char = st[idx]

    # kaam
    if seen_arr[ord(curr_char) - ord("a")] == True:
        remove_duplicate(st, idx + 1, newstr, seen_arr)

    else: 
        seen_arr[ord(curr_char) - ord("a")] = True
        remove_duplicate(st, idx + 1, newstr + curr_char, seen_arr)


seen_arr = [False] * 25

st = "banbabnanana"
newstr = ""
idx = 0
remove_duplicate(st,idx,newstr,seen_arr)

#ord function ki madad se ham character(string) ki unicode value mil jaati hai 
# print(ord("a"))   
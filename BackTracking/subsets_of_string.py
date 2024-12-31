# backtracking code to print all the subsets of a string

def str_subsets(st, new_st, idx):
    # base case
    if idx == len(st):
        if(new_st == ""):
            print("phi")
            return
        print(new_st)
        return

    # yes choice
    str_subsets(st, new_st + st[idx], idx+1)
    # no choice
    str_subsets(st, new_st, idx+1)

str_subsets("ABC","", 0)

    
def print_perm(st, idx, perm):
    # base case
    if idx == len(st):
        print(perm)
        return
    
    for i in range(len(st)):
        current = st[i]
        newstr = st[:i] + st[i+1:]
        print_perm(newstr,idx, perm + current)


st = "ABC"

print_perm(st, 0, "")

# function for alternate merging of the strings
def alternate_merging(str_one, str_two):
    i = 0
    j = 0
    flag = True
    newstr = ""
    while i < len(str_one) and j < len(str_two):
        if flag == True:
            newstr = newstr + str_one[i]
            i = i + 1
        else:
            newstr = newstr + str_two[j]
            j = j + 1
        flag = not flag

    # string one ke remaining elements ke liye loop
    while i < len(str_one):
        newstr = newstr + str_one[i]
        i = i + 1

    # string two ke remaining elements ke liye loop
    while j < len(str_two):
        newstr = newstr + str_two[j]
        j = j + 1

    return newstr


print(alternate_merging("abc", "pqr"))

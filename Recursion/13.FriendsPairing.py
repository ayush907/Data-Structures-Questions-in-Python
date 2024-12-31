
# given n friends each of one can remain single orr can be paired with some other friend. each friend can be paired only once. fiind out the total number of ways in which friends can remain single orr can be paired

def friends_pairing(n):
    # base case
    if n == 1 or n == 2: 
        return n
    
    # single
    fnm1 = friends_pairing(n - 1)

    # pair
    fnm2 = friends_pairing(n - 2)
    pair_ways = (n - 1) * fnm2

    # total ways
    total_ways = fnm1 + pair_ways

    return  total_ways


# print(friends_pairing(4))


# short code

def fp(n):
    if n == 1 or n == 2:
        return n 
    
    return fp(n - 1) + (n - 1)*fp(n - 2)      # recurrence relation

print(fp(4))



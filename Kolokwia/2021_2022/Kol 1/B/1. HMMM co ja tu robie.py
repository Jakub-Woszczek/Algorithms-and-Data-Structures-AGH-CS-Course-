def f(T):

    n = len(T)

    for i in range(n):
        T[i] = ''.join(sorted(T[i]))

    T.sort()
    max_strike = 0
    strike = 1
    el_of_strike = T[0]
    for i in range(1, n):
        if T[i] == el_of_strike:
            strike += 1

        else:
            el_of_strike = T[i]
            max_strike = max(max_strike, strike)
            strike = 1

    return max_strike

T = ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]
print(f(T))
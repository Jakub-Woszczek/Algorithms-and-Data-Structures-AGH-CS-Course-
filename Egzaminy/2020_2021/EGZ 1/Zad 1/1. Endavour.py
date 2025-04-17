def chaos_index( T ):
    def is_sorted(T):
        return sorted(T) == T

    n = len(T)
    max_strike = 0

    for k in range(n):
        if is_sorted(T) == True:
            return max(k, max_strike)
        strike = 0
        for i in range(n - 1):
            if T[i] > T[i + 1]:
                T[i], T[i + 1] = T[i + 1], T[i]
                strike += 1



            else:
                strike = 0

            max_strike = max(max_strike, strike)

    return max(k, max_strike)

x =  [5, 1, 2, 3, 4]
print(chaos_index(x))
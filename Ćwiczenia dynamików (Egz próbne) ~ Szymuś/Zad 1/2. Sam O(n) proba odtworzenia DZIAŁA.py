def roznica( S ):
    if all(c == '1' for c in S):
        return -1

    n = len(S)
    # Licze max z jedynek
    T_1 = [1 if S[i] == '1' else -1 for i in range(n)]
    T_2 = [-1 if S[i] == '1' else 1 for i in range(n)]

    def max_subsequence(T):

        max_end = T[0]
        max_so_far = T[0]
        for i in range(1,len(T)):
            max_end = max(T[i],max_end + T[i])
            max_so_far = max(max_so_far,max_end)

        return max_so_far

    return max(max_subsequence(T_1),max_subsequence(T_2))

print(roznica('11111'))
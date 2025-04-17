def maxrak(T):

    def binary_search_of_index(T,val):
        n = len(T)
        guess = n//2
        baza = n//2
        while T[guess] != val:
            if T[guess] < val:
                guess += baza//2
            else:
                guess -= baza//2
            baza //=2

    n = len(T)
    T_lewa = T[:n-1]
    # Tu trzeba posortować lewą stronę
    # mergesort(T_lewa)
    len_lewa = n-1
    max_cnt = 0
    for i in range(n-1,0,-1):
        cnt = 0
        key = T[i]
        if i <= max_cnt:
            return max_cnt



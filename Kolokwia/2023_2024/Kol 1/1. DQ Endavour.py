def maxrank(T):

    n = len(T)
    DQ = [0]*n

    for i in range(1,n):
        if T[i-1] < T[i]:
            DQ[i] = DQ[i-1] + 1

        elif T[i] == T[i-1]:
            DQ[i] = DQ[i-1]

        else:
            org = i
            while i > 0 and T[org] < T[i]:
                i -= 1

            if T[org] > T[i]:
                DQ[org] = DQ[i]+1

            elif T[org] == T[i]:
                DQ[org] = DQ[i]

            else:
                DQ[org] = 0

    print(DQ)
    return max(DQ)

T = [5,3,9,4]
print(maxrank(T))
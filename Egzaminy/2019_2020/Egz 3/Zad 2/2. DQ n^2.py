def tower(A):

    n = len(A)
    DQ = [-1 for _ in range(n)]

    for j in range(n-1):
        for i in range(j+1,n):

            x1,y1 = A[j]
            x2,y2 = A[i]

            if DQ[j] == -1:
                DQ[j] = 1

            if x1 <= x2 and y1 >= y2:
                DQ[i] = max(DQ[i],DQ[j] + 1)

    return max(DQ)


A = [(1,4),(0,5),(1,5),(2,6),(2,4)]
print(tower(A))
def falisz( T ):

    n = len(T)
    DQ = [[0]*n for _ in range(n)]

    for i in range(1,n):
        DQ[0][i] = DQ[0][i - 1] + T[0][i]
        DQ[i][0] = DQ[i - 1][0] + T[i][0]

    for i in range(1,n):
        for j in range(1,n):
            DQ[i][j] = min(DQ[i-1][j],DQ[i][j-1]) + T[i][j]

    return DQ[n-1][n-1]
def parking(X,Y): # 1.04sec

    n = len(X)
    m = len(Y)
    DQ = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]

    # Min suma przy 0 budynkach to zero
    for i in range(m + 1):
        DQ[0][i] = 0

    for i in range(1, n + 1):
        for j in range(i,
                       m + 1):  # Biorąc od i do m unikam sytuacji gdzie rozpatruje mniejszą ilość parkingów od budynków
            DQ[i][j] = min(DQ[i][j - 1], DQ[i - 1][j - 1] + abs(X[i - 1] - Y[j - 1]))

    return DQ[n][m]
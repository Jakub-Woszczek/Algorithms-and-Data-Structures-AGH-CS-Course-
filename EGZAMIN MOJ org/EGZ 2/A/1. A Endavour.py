def wired(T):
    n = len(T)

    # Ustawiam tablice gdzie mam zapisaną różnice mocy między każdymi dwoma wejściami
    T_roznicy_mocy = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(n):
            if i != j:
                T_roznicy_mocy[j][i][0] = abs(T[i] - T[j])
                T_roznicy_mocy[i][j][0] = abs(T[i] - T[j])

















T = [7,1,3,7,2,1]
wired(T)
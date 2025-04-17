from zad1ktesty import runtests

def roznica( S ):
    print(S)
    def czy_sama_jedynki(liczba_binarna):
        return all(znak == '1' for znak in liczba_binarna)

    if czy_sama_jedynki(S) == True:
        return -1

    # Ustawienie tabicy dynamicznej
    n = len(S)
    DQ = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        DQ[i][i] = [1, 0] if S[i] == '0' else [0, 1]

    max_diffrence = 0
    # Biedne n^2
    for i in range(n):
        for j in range(i + 1, n):
            DQ[i][j] = [DQ[i][j - 1][0] + 1, DQ[i][j - 1][1]] if DQ[j][j][0] == 1 else [DQ[i][j - 1][0],
                                                                                        DQ[i][j - 1][1] + 1]
            max_diffrence = max(max_diffrence, abs(DQ[i][j][0] - DQ[i][j][1]))

    return max_diffrence
    return 0

runtests ( roznica )
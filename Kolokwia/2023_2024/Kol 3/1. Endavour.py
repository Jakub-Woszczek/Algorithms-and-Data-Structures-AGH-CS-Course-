def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)


def orchard(T, m):
    n = len(T)

    # Tablica dynamicznego programowania: DQ[mod][i] to minimalna liczba wyciętych drzew
    # dla sumy modulo 'mod' po uwzględnieniu pierwszych i drzew
    DQ = [[float('inf')] * (n + 1) for _ in range(m)]

    # Na początku nie wycięto żadnych drzew i suma jabłek wynosi 0 (mod m)
    DQ[0][0] = 0

    for i in range(n):
        for mod in range(m):
            if DQ[mod][i] < float('inf'):
                # Drzewo jest pomijane (nie wycinamy go)
                new_mod = (mod + T[i]) % m
                DQ[new_mod][i + 1] = min(DQ[new_mod][i + 1], DQ[mod][i])

                # Drzewo jest wycięte
                DQ[mod][i + 1] = min(DQ[mod][i + 1], DQ[mod][i] + 1)

    # Minimalna liczba wyciętych drzew, aby uzyskać sumę podzielną przez m
    return DQ[0][n] if DQ[0][n] != float('inf') else n

T = [2, 2, 7, 5, 1, 14, 7]
m = 7

orchard(T,m)
def print_2d_array(array):
    # Znajdź maksymalną długość elementu w tablicy
    max_len = max(len(str(element)) for row in array for element in row)

    # Iteracja po wierszach
    for row in array:
        # Tworzenie wiersza jako sformatowany string
        formatted_row = " ".join(f"{str(element):>{max_len}}" for element in row)
        print(formatted_row)

def parking(X, Y): # 0.8 sec
    n = len(X)
    m = len(Y)
    DQ = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]

    # Min suma przy 0 budynkach to zero
    for i in range(m + 1):
        DQ[0][i] = 0

    for i in range(1, n + 1):
        for j in range(i,
                       m + 1):  # Biorąc od i do m unikam sytuacji gdzie rozpatruje mniejszą ilość parkingów od budynków
            if DQ[i][j - 1] == DQ[i][j - 2] and j > i + 2:
                DQ[i][j] = DQ[i][j - 1]
            else:
                DQ[i][j] = min(DQ[i][j - 1], DQ[i - 1][j - 1] + abs(X[i - 1] - Y[j - 1]))

    return DQ[n][m]

Pozycje_biurowcow=[21, 28, 34, 41, 47, 50, 60, 69, 71, 78]
Pozycje_dzialek=[11, 14, 20, 21, 25, 30, 32, 35, 37, 38, 42, 43, 49, 50, 52, 53, 57, 58, 60, 61]

T = parking(Pozycje_biurowcow,Pozycje_dzialek)

print_2d_array(T)
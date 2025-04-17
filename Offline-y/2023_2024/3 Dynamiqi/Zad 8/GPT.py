def parking(X, Y):
    n = len(X)
    m = len(Y)

    # Tworzymy dp z rozmiarami (n+1) x (m+1), wypełnione dużymi wartościami (inf)
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Inicjalizujemy dp[0][j] na 0, gdyż przypisanie 0 biurowców wymaga 0 kosztów
    for j in range(m + 1):
        dp[0][j] = 0

    # Wypełniamy tablicę dp
    for i in range(1, n + 1):
        for j in range(i, m + 1):  # j musi być co najmniej i, aby mieć co przypisać
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1] + abs(X[i - 1] - Y[j - 1]))

    # Ostateczna odpowiedź to minimalny koszt przypisania wszystkich n biurowców z m działek
    return dp[n][m]


# Przykład użycia
X = [3, 6, 10, 14]
Y = [1, 4, 5, 10, 11, 13, 17]
print(parking(X, Y))  # Wynik powinien wynosić 3

def print_dp(dp):
    # Funkcja, która ładnie drukuje macierz dp
    print("Aktualna macierz dp:")
    for row in dp:
        print(" ".join(f"{val if val != float('inf') else 'inf':>6}" for val in row))
    print()  # Dodatkowa linia dla czytelności


def wired(T):
    n = len(T)

    # Sprawdzenie, czy n jest parzyste
    if n % 2 != 0:
        raise ValueError("Liczba wejść musi być parzysta!")

    # Inicjalizacja macierzy dp
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]

    # Inicjalizacja macierzy dla sąsiednich elementów
    for i in range(n - 1):
        dp[i][i + 1] = 1 + abs(T[i] - T[i + 1])
        print(f"Połączenie sąsiednich wejść {i} i {i + 1} kosztuje: {dp[i][i + 1]}")

    print_dp(dp)  # Drukowanie dp po inicjalizacji dla sąsiednich elementów

    # Algorytm dynamicznego programowania dla większych przedziałów
    for i in range(n // 2 - 1):
        for j in range(n - 3 - 2 * i):
            # Aktualizacja dp dla większych przedziałów
            dp[j][j + 3 + 2 * i] = dp[j + 1][j + 2 + 2 * i] + 1 + abs(T[j] - T[j + 3 + 2 * i])
            print(f"Połączenie wejść {j} i {j + 3 + 2 * i} kosztuje: {dp[j][j + 3 + 2 * i]}")

            # Szukanie minimalnego kosztu połączeń dla przedziału
            for k in range(j + 2, j + 4 + 2 * i, 2):
                stary_koszt = dp[j][j + 3 + 2 * i]
                dp[j][j + 3 + 2 * i] = min(dp[j][j + 3 + 2 * i], dp[j][k - 1] + dp[k][j + 3 + 2 * i])
                nowy_koszt = dp[j][j + 3 + 2 * i]

                if nowy_koszt < stary_koszt:
                    print(f"Znaleziono lepsze połączenie dla wejść {j} i {j + 3 + 2 * i} "
                          f"przez rozbicie na przedziały [{j}, {k - 1}] i [{k}, {j + 3 + 2 * i}]")

            # Drukowanie aktualnej macierzy dp po każdej iteracji
            print_dp(dp)

    # Wynik końcowy
    print(f"Minimalny koszt połączenia wszystkich wejść: {dp[0][n - 1]}")

    return dp[0][n - 1]


# Przykład użycia
T = [7,1,3,7,2,1]
print("Lista mocy wejść:", T)
minimalny_koszt = wired(T)
print("Minimalny koszt:", minimalny_koszt)

# Jakub Woszczek

# Mój algorytm polega na stworzeniu tablicy DQ o szerokości m = ilośći parkingów i długości n = ilość budynków
# Tak jak w podpowiedzi DQ[i][j] przedstawia najkrótszą sume gdy biurowiec i ma parking j-ty. Dwie pętle przechodzą
# po wszystkich możliwych parkingach j dla i-tego budynku. Dla 0 budynków jest 0.
# No i DQ[i][j] to min z [komórki z lewej ( wersja gdy nie bierzemy danego parkingu ) i D[i-1][j-1] + odległość z i-tego budynku do j-tego parkingu]
# Więć komórka D[n][m] reprezentuje więc minimalną sume dla n budynków i m parkingów.
# Usprawnienie_______ jezeli powtóży się w rzędzie już 2 razy ta sama liczba to ją dalej przepisuje bo parkingi są posortowane
# Szacuje złożoność mojego algorytmu na O(n*m)

from zad8testy import runtests

def parking(X, Y):
  n = len(X)
  m = len(Y)
  DQ = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]

  # Min suma przy 0 budynkach to zero
  for i in range(m + 1):
    DQ[0][i] = 0

  for i in range(1, n + 1):
    for j in range(i, m + 1):  # Biorąc od i do m unikam sytuacji gdzie rozpatruje mniejszą ilość parkingów od budynków
      if DQ[i][j - 1] == DQ[i][j - 2] and j > i + 2:
        DQ[i][j] = DQ[i][j - 1]
      else:
        DQ[i][j] = min(DQ[i][j - 1], DQ[i - 1][j - 1] + abs(X[i - 1] - Y[j - 1]))

  return DQ[n][m]
  pass

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )

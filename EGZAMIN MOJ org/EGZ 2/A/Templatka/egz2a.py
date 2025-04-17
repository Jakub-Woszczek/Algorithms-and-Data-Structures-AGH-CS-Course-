# Jakub Woszczek

# Implementacja polega na funkcji rekurencyjnej która jednym forem
# przechodzi po tablicy i dla każdego 'i' dzieli na 2 mniejsze
# i w tych mniejszych też jest for .....

# Złożoność to O(2^n*poly(n))


from egz2atesty import runtests


def wired( T ):
  n = len(T)

  # Ustawiam tablice gdzie mam zapisaną różnice mocy między każdymi dwoma wejściami
  T_roznicy_mocy = [[0 for _ in range(n)] for _ in range(n)]

  all_voltage = 0

  for j in range(n):
    for i in range(n):
      if i != j:
        T_roznicy_mocy[j][i] = abs(T[i] - T[j])
        T_roznicy_mocy[i][j] = abs(T[i] - T[j])

  def min_z_T(T):

    nonlocal all_voltage
    lenght = len(T)
    if lenght == 2:
      return T_roznicy_mocy[T[0]][T[1]]

    suma_curr = T[0] + T[len(T) - 1]
    for i in range(1, lenght, 2):
      suma_curr += min(min_z_T(T[i:]) + min_z_T(T[i:]))

    return suma_curr

  suma_min = float('inf')

  for i in range(1, n, 2):
    suma_min = min(min_z_T(T[i:]) + min_z_T(T[i:]), suma_min)

  return suma_min
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = False )

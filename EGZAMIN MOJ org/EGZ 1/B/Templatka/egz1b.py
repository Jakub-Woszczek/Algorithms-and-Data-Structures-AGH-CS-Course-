# Jakub Woszczek

# Algorytm opiera się na znajdowaniu wszystkich możliwych podciągów w ten sposób
# że przeskakuje dwoma while-ami z lewej a w nim z prawej tak by przejść po ujemnych
#   i dodatkich. i ze wszystkich możliwych wycinków Dynamicznie w 'max_sum_bez_k' biore
# max z tej tablicy

# Złożoność szacuje na O(n^2)




from egz1btesty import runtests


def kstrong( T, k):
  n = len(T)

  DQ = [[0 for _ in range(n)] for _ in range(k + 1)]

  DQ[0][0] = T[0]

  for i in range(1, n):
    DQ[0][i] = max(DQ[0][i - 1] + T[i], T[i])

  for i in range(0, k):
    DQ[i + 1][i] = 0

  overall_max = 0

  for row in range(1, k + 1):
    for col in range(row, n):
      DQ[row][col] = max(DQ[row - 1][col - 1], DQ[row][col - 1] + T[col])
      overall_max = max(overall_max, DQ[row][col])

  return overall_max

  return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )

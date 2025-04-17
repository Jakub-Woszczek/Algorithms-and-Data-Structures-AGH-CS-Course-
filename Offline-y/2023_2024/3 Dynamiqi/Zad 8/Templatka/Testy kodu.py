# Jakub Woszczek

from zad8testy import runtests

def parking(X,Y):
  n = len(X)
  m = len(Y)
  DQ = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]

  # Min suma przy 0 budynkach to zero
  for i in range(m + 1):
    DQ[0][i] = 0

  for i in range(1, n + 1):
    for j in range(i, m + 1):  # Biorąc od i do m unikam sytuacji gdzie rozpatruje mniejszą ilość parkingów od budynków
      if DQ[i][j-1] == DQ[i][j - 2] and j > i + 2:
        DQ[i][j] =  DQ[i][j-1]
      else:
        DQ[i][j] = min(DQ[i][j - 1], DQ[i - 1][j - 1] + abs(X[i - 1] - Y[j - 1]))

      # print_2d_array(DQ)
    # print_2d_array(DQ)
  # return DQ
  return DQ[n][m]
  pass

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )

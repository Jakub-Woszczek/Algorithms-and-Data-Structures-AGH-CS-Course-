from egz1btesty import runtests


def kstrong( T, k):
  if k == len(T):
    sumA = 0
    for el in T:
      if el > 0:
        sumA += el
    return sumA

  n = len(T)

  DQ = [0] * (n + 1)

  DQ[0] = T[0] if T[0] > 0 else 0

  for i in range(1, n):
    DQ[i] = DQ[i - 1] + T[i] if DQ[i - 1] + T[i] > 0 else 0

  for k in range(1, k + 1):
    erased_prev = DQ[k]
    DQ[k] = max(DQ[k - 1], T[k])

    for i in range(k, n):
      erased = DQ[i]
      DQ[i] = max(DQ[i - 1] + T[i], erased_prev)
      erased_prev = erased

  print(DQ)
  return max(DQ)
  return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )

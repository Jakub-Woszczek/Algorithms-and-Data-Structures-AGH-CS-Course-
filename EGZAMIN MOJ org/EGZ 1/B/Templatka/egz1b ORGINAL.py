# Jakub Woszczek

# Algorytm opiera się na znajdowaniu wszystkich możliwych podciągów w ten sposób
# że przeskakuje dwoma while-ami z lewej a w nim z prawej tak by przejść po ujemnych
#   i dodatkich. i ze wszystkich możliwych wycinków Dynamicznie w 'max_sum_bez_k' biore
# max z tej tablicy

# Złożoność szacuje na O(n^2)




from egz1btesty import runtests


def kstrong( T, k):
  def max_sum_bez_k(T, k):

    if len(T) < k:
      return 0

    n = len(T)
    DQ = [[0 for _ in range(n)] for _ in range(k)]
    DQ[0][0] = T[0]

    for i in range(n):
      DQ[0][i] = DQ[0][i - 1] + T[i]

    for row in range(1, k):

      for j in range(row, n):
        DQ[row][j] = max(DQ[row][j - 1] + T[j], DQ[row - 1][j - 1])

    max_val = 0
    for i in range(k):
      max_val = max(max_val, DQ[i][n - 1])
    return max_val

  # Spr czy lenTslice > k:
  n = len(T)
  max_k_spojny = 0
  start, end = 0, n

  if T[start] >= 0 and T[end - 1] >= 0:

    while start < n:
      end = n
      max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))
      while start < end:
        end -= 1

        while end >= 0 and not (T[end] < 0 and T[end - 1] > 0):
          end -= 1

        # SPR
        max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))
      start += 1
      while start < n and not (T[start] > 0 and T[start - 1] < 0):
        start += 1

  start, end = 0, n

  if T[start] >= 0 and T[end - 1] < 0:
    end -= 1
    while end >= 0 and not (T[end] < 0 and T[end - 1] > 0):
      end -= 1

    max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))

    while start < n:
      end = n
      max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))
      while start < end:
        end -= 1

        while end >= 0 and not (T[end] < 0 and T[end - 1] > 0):
          end -= 1

        # SPR
        max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))
      start += 1
      while start < n and not (T[start] > 0 and T[start - 1] < 0):
        start += 1

  start, end = 0, n

  if T[start] < 0 and T[end - 1] >= 0:
    while start < n and not (T[start] > 0 and T[start - 1] < 0):
      start += 1

    print(f'spr {T[start:end]}')
    max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))

    while start < n:
      end = n
      print(f'spr {T[start:end]}')
      max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))
      while start < end:
        end -= 1

        while end >= 0 and not (T[end] < 0 and T[end - 1] > 0):
          end -= 1

        # SPR
        print(f'spr {T[start:end]}')
        max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))
      start += 1
      while start < n and not (T[start] > 0 and T[start - 1] < 0):
        start += 1

  start, end = 0, n

  if T[start] < 0 and T[end - 1] < 0:

    while start < n and not (T[start] > 0 and T[start - 1] < 0):
      start += 1

    end -= 1
    while end >= 0 and not (T[end] < 0 and T[end - 1] > 0):
      end -= 1

    max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))

    while start < n:
      end = n
      max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))
      while start < end:
        end -= 1

        while end >= 0 and not (T[end] < 0 and T[end - 1] > 0):
          end -= 1

        # SPR
        max_k_spojny = max(max_k_spojny, max_sum_bez_k(T[start:end], k))
      start += 1
      while start < n and not (T[start] > 0 and T[start - 1] < 0):
        start += 1

  return max_k_spojny
  return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = False )

from kol3testy import runtests


def orchard(T, m):
    T_left = []
    for el in T:
        if el % m != 0:
            T_left.append(el)

    n = len(T_left)
    DQ = [[float('inf') for _ in range(n)] for _ in range(m)]

    DQ[0][0] = 1
    DQ[T_left[0] % m][0] = 0

    for col in range(n - 1):
        for row in range(m):
            if DQ[row][col] < float('inf'):
                curr_cuted = DQ[row][col]
                three = T_left[col + 1]

                # Ścinam
                DQ[row][col + 1] = min(DQ[row][col + 1], curr_cuted + 1)

                # Nie ścinam
                DQ[(row + three) % m][col + 1] = min(DQ[(row + three) % m][col + 1], curr_cuted)



    return DQ[0][n-1]
    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)

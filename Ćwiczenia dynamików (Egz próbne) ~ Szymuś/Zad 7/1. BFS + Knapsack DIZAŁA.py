def ogrodnik( T, D, Z, l ):
    rows = len(T)
    cols = len(T[0])

    def suma_korzenia(T, x_coordinate):
        from queue import Queue
        been_here = set()
        Q = Queue()  # W środku będą krotki typu (poziom (y_cord), x_cord)
        Q.put((0, x_coordinate))
        overall_sum = 0
        posibilities = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]

        while not Q.empty():
            y_cord, x_cord = Q.get()
            if 0 <= y_cord < rows and 0 <= x_cord < cols:
                overall_sum += T[y_cord][x_cord]
                been_here.add((y_cord, x_cord))

                for y, x in posibilities:
                    new_y = y_cord + y
                    new_x = x_cord + x

                    if 0 <= new_y < rows and 0 <= new_x < cols and (new_y, new_x) not in been_here and T[new_y][
                        new_x] != 0:
                        Q.put((new_y, new_x))
                        been_here.add((new_y, new_x))  # Dodajemy od razu po włożeniu do kolejki

        return overall_sum

    n = len(D)
    koszt_drzewa = [0] * n

    for i in range(n):
        koszt_drzewa[i] = suma_korzenia(T, D[i])

    Zysk = Z

    DQ = [[0] * (n) for _ in range(l + 1)]

    for i in range(l):
        DQ[i][0] = 0 if i < koszt_drzewa[0] else Zysk[0]

    for col in range(1, n):
        for row in range(1, l + 1):
            val_1 = max(DQ[row][col - 1], DQ[row - 1][col])
            if row >= koszt_drzewa[col]:
                val_2 = DQ[row - koszt_drzewa[col]][col - 1] + Zysk[col]
            else:
                val_2 = 0

            DQ[row][col] = max(val_1, val_2)

    for bruh in DQ:
        print(bruh)
    print('')

    return DQ[l][n - 1]



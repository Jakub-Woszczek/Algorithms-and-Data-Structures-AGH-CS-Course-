# Jakub Woszczek

# Mój algorytm opiera się na uaktulanianiu po kolei każdej kolumny od lewej do prawej strony ( dokładniej w pseudokodzie)
# Szacuje złożoność na O(n^2) gdzie   n = len(L)

# ________Pseudokod_______
# 1. Przygotowanie
# - Zamieniam z mapy '..#.' na [0,0,None,0] złożonej z None i 0 gdzie  .=0 i #=None
# - Zamieniam pola nieosiągalne z komóki [0,0] i [n-1,n-1] na None !
#
# 2. Algorytm
# - Ustawiam pierwszą ścieżke w dół z pola [0,0]

# FOR each col ->
# 	FOR each row (downward)
# 		Przepisuje jak można pole z lewej + 1
# 	FOR each row (downward) Najdłuższa scieżka w dół
# 		Aktualizuje każdą max(curr,prev + 1)
# 	FOR each row (upward) Najdłuższa ścieżka w góre
# 		if cuur == None:
# 			seed = 0
# 		else:
#           if seed != 0:
# 			    seed += 1
# 			if lewy != None:
# 				seed = max(seed,lewy + 1)
# 			cuur = max(seed,curr)


from zad7testy import runtests
def maze( L ):
    def z_kropek_na_zera(Hash_map):
        n = len(Hash_map)
        Labi = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if Hash_map[i][j] == '#':
                    Labi[i][j] = None

        return Labi
    def wypelnianie_niedostepnych(Labi):
        from collections import deque
        def Wypelnij_niedostepne_Nonami_lewy_gorny(Labirynt):
            n = len(Labirynt)
            m = len(Labirynt[0]) if n > 0 else 0

            # BFS
            queue = deque([(0, 0)])
            while queue:
                x, y = queue.popleft()
                if Labirynt[x][y] == 0:
                    Labirynt[x][y] = 'V'  # 'V' oznacza, że komórka była odwiedzona

                    # Sprawdzanie sąsiadów
                    for dx, dy in [(0, 1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and Labirynt[nx][ny] == 0:
                            queue.append((nx, ny))

            # Oznaczanie niedostępnych komórek jako None
            for i in range(n):
                for j in range(m):
                    if Labirynt[i][j] == 0:
                        Labirynt[i][j] = None
                    elif Labirynt[i][j] == 'V':
                        Labirynt[i][j] = 0

            return Labirynt

        def Wypelnij_niedostepne_Nonami_prawny_dolny(Labirynt):
            n = len(Labirynt)
            m = len(Labirynt[0]) if n > 0 else 0

            # BFS starting from T[n-1][n-1]
            queue = deque([(n - 1, n - 1)])
            while queue:
                x, y = queue.popleft()
                if Labirynt[x][y] == 0:
                    Labirynt[x][y] = 'V'  # 'V' oznacza, że komórka była odwiedzona

                    # Sprawdzanie sąsiadów
                    for dx, dy in [(0, -1), (-1, 0), (1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and Labirynt[nx][ny] == 0:
                            queue.append((nx, ny))

            # Oznaczanie niedostępnych komórek jako None
            for i in range(n):
                for j in range(m):
                    if Labirynt[i][j] == 0:
                        Labirynt[i][j] = None
                    elif Labirynt[i][j] == 'V':
                        Labirynt[i][j] = 0

            return Labirynt

        Labi = Wypelnij_niedostepne_Nonami_lewy_gorny(Labi)
        Labi = Wypelnij_niedostepne_Nonami_prawny_dolny(Labi)

        return Labi

    DQ = z_kropek_na_zera(L) # Zamieniam na zaera i None
    DQ = wypelnianie_niedostepnych(DQ) # Wypełniam niedostępne miejsca None-ami
    n = len(L)

    ### ALGORYTM ###

    #___________ PIERWSZA KOLUMNA W DÓŁ __________#

    row = 1
    while row < n and DQ[row][0] != None:
        DQ[row][0] = DQ[row - 1][0] + 1
        row += 1



    # ___________ GŁÓWNA PĘTLA DLA KAŻDEJ KOLUMNY __________#

    for col in range(1,n):

        # ___________ PRZEPISANIE LEWEJ STRONY + 1 __________#
        for down_row_1 in range(n):
            if DQ[down_row_1][col] != None and DQ[down_row_1][col-1] != None:
                DQ[down_row_1][col] = DQ[down_row_1][col-1] + 1


        # ___________ NJADŁUŻSZA ŚCIEŻKA W DÓŁ __________#
        for down_row_path in range(1,n):
            if DQ[down_row_path][col] != None and DQ[down_row_path-1][col] != None:
                DQ[down_row_path][col] = max(DQ[down_row_path][col],DQ[down_row_path-1][col]+1)


        # ___________ NJADŁUŻSZA ŚCIEŻKA W GÓRE __________#
        seed = 0
        for up_row in range(n-1,-1,-1):

            if DQ[up_row][col] == None:
                seed = 0

            else:
                if seed != 0:
                    seed += 1

                if DQ[up_row][col - 1] != None:
                    seed = max(seed,DQ[up_row][col - 1] + 1)

                DQ[up_row][col] = max(seed,DQ[up_row][col])

    return DQ[n - 1][n - 1] if DQ[n - 1][n - 1] != None else -1
    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )

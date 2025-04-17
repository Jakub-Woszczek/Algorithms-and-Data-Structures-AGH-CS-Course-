from collections import deque

def goodknight(G, s, t):
    def min_wartosc_w_ostatniej_kolumnie(tablica):
        min_wartosc = float('inf')
        for wiersz in tablica:
            wartosc = wiersz[-1]
            if wartosc < min_wartosc:
                min_wartosc = wartosc
        return min_wartosc

    def macierz_na_liste_sasiedztwa(G):
        T = []
        for i in range(len(G)):
            sasiad = []
            for j in range(len(G[i])):
                if G[i][j] != -1:
                    sasiad.append([j, G[i][j]])
            T.append(sasiad)
        return T

    max_tirednesss = 16
    n = len(G)
    DQ = [[float('inf') for _ in range(n)] for _ in range(max_tirednesss + 1)]
    T_sons = macierz_na_liste_sasiedztwa(G)

    # Kolejka BFS: (tiredness, vertex, current_time)
    queue = deque()

    # Inicjalizujemy BFS dla zamku startowego s
    DQ[0][s] = 0
    queue.append((0, s, 0))

    while queue:
        curr_tiredness, curr_vertex, curr_time = queue.popleft()

        # Przeglądaj sąsiadów bieżącego wierzchołka
        for Next_col, Edge_w in T_sons[curr_vertex]:
            new_tiredness = curr_tiredness + Edge_w
            new_time = curr_time + Edge_w

            if new_tiredness <= max_tirednesss:
                # Jeśli znaleziono krótszą drogę do sąsiada z określonym zmęczeniem
                if new_time < DQ[new_tiredness][Next_col]:
                    DQ[new_tiredness][Next_col] = new_time
                    queue.append((new_tiredness, Next_col, new_time))

                # Sprawdzenie noclegu (jeśli zmęczenie >= 8)
                if new_tiredness >= 8:
                    rest_tiredness = new_tiredness - 8
                    rest_time = new_time + 8  # Dodajemy 8 godzin na odpoczynek
                    if rest_time < DQ[rest_tiredness][Next_col]:
                        DQ[rest_tiredness][Next_col] = rest_time
                        queue.append((rest_tiredness, Next_col, rest_time))

    return min_wartosc_w_ostatniej_kolumnie(DQ)

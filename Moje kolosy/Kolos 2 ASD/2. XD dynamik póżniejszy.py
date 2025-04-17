def warrior( G, s, t):
    def min_wartosc_w_ostatniej_kolumnie(tablica):
        min_wartosc = float('inf')
        for wiersz in tablica:
            wartosc = wiersz[-1]
            if wartosc < min_wartosc:
                min_wartosc = wartosc
        return min_wartosc

    def lista_krawedzi_na_liste_sasiedztwa(G):
        # Znajdujemy maksymalny numer wierzchołka, aby wiedzieć, ile potrzebujemy list
        max_wierzcholek = max(max(u, v) for u, v, w in G)

        # Tworzymy pustą tablicę sąsiedztwa z odpowiednią liczbą pustych list
        T = [[] for _ in range(max_wierzcholek + 1)]

        # Dodajemy każdą krawędź do tablicy sąsiedztwa
        for u, v, w in G:
            T[u].append((v, w))

        return T

    max_tirednesss = 16
    n = len(G[0])
    DQ = [[float('inf') for _ in range(n)] for _ in range(max_tirednesss + 1)]
    T_sons = lista_krawedzi_na_liste_sasiedztwa(G)

    # Prep zerowy wirzchołek
    for i in range(max_tirednesss + 1):
        DQ[i][0] = 0

    for sonsiad, edge in T_sons[0]:
        DQ[0][sonsiad] = edge + 8
        print(edge)
        DQ[edge][sonsiad] = edge

    for Column in range(1, n):  # Curr vertex
        for Rows in range(max_tirednesss + 1):  # Curr tiredness
            if DQ[Rows][Column] < float('inf'):
                curr_cost = DQ[Rows][Column]

                for Next_col, Edge_w in T_sons[Column]:
                    if Rows + Edge_w <= max_tirednesss:
                        DQ[Rows + Edge_w][Next_col] = min(curr_cost + Edge_w, DQ[Rows + Edge_w][Next_col])
                        DQ[0][Next_col] = min(DQ[Rows + Edge_w][Next_col] + 8, DQ[0][Next_col])

    return min_wartosc_w_ostatniej_kolumnie(DQ)
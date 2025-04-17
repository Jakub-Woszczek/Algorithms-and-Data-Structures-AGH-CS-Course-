def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def goodknight( G, s, t ):
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
    n = len(G[0])
    DQ = [[float('inf') for _ in range(n)] for _ in range(max_tirednesss+1)]
    T_sons = macierz_na_liste_sasiedztwa(G)

    # Prep zerowy wirzchołek
    for i in range(max_tirednesss+1):
        DQ[i][0] = 0

    for sonsiad, edge in T_sons[0]:
        DQ[0][sonsiad] = edge+8
        print(edge)
        DQ[edge][sonsiad] = edge

    for Column in range(1,n): # Curr vertex
        for Rows in range(max_tirednesss + 1): # Curr tiredness
            if DQ[Rows][Column] < float('inf'):
                curr_cost = DQ[Rows][Column]

                for Next_col,Edge_w in T_sons[Column]:
                    if Rows+Edge_w <= max_tirednesss:
                        DQ[Rows+Edge_w][Next_col] = min(curr_cost+Edge_w,DQ[Rows+Edge_w][Next_col])
                        DQ[0][Next_col] = min(DQ[Rows+Edge_w][Next_col]+8,DQ[0][Next_col])

    return min_wartosc_w_ostatniej_kolumnie(DQ)
    # print_straight(DQ)


G = [ [ -1, 3, 8,-1,-1,-1 ], # 0
[ 3,-1, 3, 6,-1,-1 ], # 1
[ 8, 3,-1,-1, 5,-1 ], # 2
[ -1, 6,-1,-1, 7, 8 ], # 3
[ -1,-1, 5, 7,-1, 8 ], # 4
[ -1,-1,-1, 8, 8,-1 ]] # 5
s = 0
t = 5


goodknight(G,s,t)
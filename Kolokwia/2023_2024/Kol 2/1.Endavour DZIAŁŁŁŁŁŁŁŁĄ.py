def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in
                     range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)


def warrior(G, s, t):
    def edges_to_adjacency_list(edges):
        """Konwersja listy krawędzi na listę sąsiedztwa."""
        # Znalezienie maksymalnego wierzchołka w grafie
        max_vertex = max(max(u, v) for u, v, _ in edges)

        # Tworzenie pustej listy sąsiedztwa dla każdego wierzchołka
        adjacency_list = [[] for _ in range(max_vertex + 1)]

        # Dodawanie sąsiadów do odpowiednich list
        for u, v, val in edges:
            adjacency_list[u].append((v, val))  # Dodajemy v jako sąsiada u
            adjacency_list[v].append((u, val))  # Dodajemy u jako sąsiada v (graf nieskierowany)

        return adjacency_list

    """Funkcja, która zwraca liczbę godzin najszybszej drogi z s do t, zgodnie z zasadami."""
    from queue import PriorityQueue

    # Konwersja listy krawędzi na listę sąsiedztwa
    G_sons = edges_to_adjacency_list(G)
    n = len(G_sons)

    # Tablica na odległości z indeksowaniem na podstawie zmęczenia
    DQ = [[None for _ in range(n)] for _ in range(17)]
    Q = PriorityQueue()

    # Inicjalizacja początkowego stanu
    DQ[0][s] = 0  # Na początku wojownik jest wypoczęty i startuje z s
    Q.put((0, 0, s))  # (dystans, zmęczenie, wierzchołek)

    while not Q.empty():
        curr_dist, tiredness, curr_v = Q.get()

        for somsiad,edge in G_sons[curr_v]:

            new_tiredness = tiredness + edge

            if new_tiredness < 17:

                if DQ[new_tiredness][somsiad] == None or DQ[new_tiredness][somsiad] > curr_dist + edge:
                    DQ[new_tiredness][somsiad] = curr_dist + edge
                    Q.put((curr_dist+edge,new_tiredness,somsiad))

                if DQ[0][somsiad] == None or DQ[0][somsiad] > curr_dist + edge + 8:
                    DQ[0][somsiad] = curr_dist + edge + 8
                    Q.put((curr_dist + edge + 8, 0, somsiad))






    print_straight(DQ)
    min_end = float('inf')
    for i in range(17):
        if DQ[i][t] is not None:
            min_end = min(min_end, DQ[i][t])

    return min_end


G = [(1, 5, 10), (4, 6, 12), (3, 2, 8),
     (2, 4, 4), (2, 0, 10), (1, 4, 5),
     (1, 0, 6), (5, 6, 8), (6, 3, 9)]
s = 0
t = 6
print(warrior(G,s,t))
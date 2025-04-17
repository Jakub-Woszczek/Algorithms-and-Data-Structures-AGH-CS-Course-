def armstrong(G,B,s,t):

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

    G_sons = edges_to_adjacency_list(G)

    def dikstria(G_sons,start):
        from queue import PriorityQueue

        n = len(G_sons)
        Q = PriorityQueue()
        all_dist = [float('inf')] * n  # Tablica dystansów
        been_here = [False] * n  # Tablica odwiedzonych wierzchołków
        all_dist[start] = 0  # Dystans do samego siebie to 0

        Q.put((0, start))  # Kolejka priorytetowa: (dystans, wierzchołek)

        while not Q.empty():
            curr_dist, curr_v = Q.get()  # Pobierz wierzchołek o najmniejszym dystansie

            if been_here[curr_v]:
                continue  # Jeśli już byliśmy w tym wierzchołku, przejdź dalej

            been_here[curr_v] = True  # Zaznacz wierzchołek jako odwiedzony

            # Sprawdź sąsiadów wierzchołka
            for neighbor, edge in G_sons[curr_v]:
                if not been_here[neighbor]:
                    new_dist = curr_dist + edge  # Oblicz nowy dystans
                    if new_dist < all_dist[neighbor]:
                        all_dist[neighbor] = new_dist  # Zaktualizuj dystans
                        Q.put((new_dist, neighbor))  # Dodaj do kolejki nowy dystans i wierzchołek

        return all_dist

    from_start = dikstria(G_sons,s)
    from_end = dikstria(G_sons,t)

    min_path = float('inf')
    for vertex,p,q in B:
        min_path = min(min_path,from_start[vertex] + (from_end[vertex]*p/q)//1)
        print(from_start[vertex] + (from_end[vertex]*p/q))



    return min(min_path,from_start[t])



B = [[1,1,2],[2,2,3]]
G = [[0,1,6],[1,4,7],[4,3,4],[3,2,4],[2,0,3],[0,3,6]]


B_2 = [(6, 181, 91), (9, 160, 162), (4, 147, 141), (7, 186, 140), (8, 217, 79)]
G_2 = [(0, 1, 39), (0, 2, 26), (0, 3, 28), (0, 4, 34), (0, 5, 46), (0, 6, 35), (0, 7, 14), (0, 8, 33), (0, 9, 43), (1, 2, 18), (1, 3, 41), (1, 4, 27), (1, 5, 29), (1, 6, 19), (1, 7, 53), (1, 8, 19), (1, 9, 41), (2, 3, 29), (2, 4, 16), (2, 5, 30), (2, 6, 30), (2, 7, 18), (2, 8, 34), (2, 9, 38), (3, 4, 51), (3, 5, 33), (3, 6, 33), (3, 7, 38), (3, 8, 37), (3, 9, 26), (4, 5, 28), (4, 6, 22), (4, 7, 33), (4, 8, 34), (4, 9, 43), (5, 6, 24), (5, 7, 48), (5, 8, 21), (5, 9, 33), (6, 7, 29), (6, 8, 14), (6, 9, 27), (7, 8, 37), (7, 9, 28), (8, 9, 28)]
# s = 0
# t = 4
s = 4
t = 3
# 45
print(armstrong(G_2,B_2,s,t))
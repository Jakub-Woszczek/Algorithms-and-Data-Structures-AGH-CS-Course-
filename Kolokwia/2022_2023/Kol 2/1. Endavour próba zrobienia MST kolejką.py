def beautree(G):
    from queue import PriorityQueue
    def edges_from_graph(G):
        edges = []
        visited = set()  # Zbiór do śledzenia odwiedzonych krawędzi

        for u in range(len(G)):  # Iteracja po wierzchołkach
            for v, weight in G[u]:  # Iteracja po sąsiadach wierzchołka u
                if (v, u) not in visited:  # Sprawdzamy, czy krawędź nie była już odwiedzona
                    edges.append((u, v, weight))
                    visited.add((u, v))  # Dodajemy krawędź do odwiedzonych

        return edges

    def find_smallest_edge(G):
        v1, v2, edge_prime = None, None, float('inf')

        for i, neighbors in enumerate(G):  # Używamy enumerate zamiast ręcznego liczenia indeksów
            for v, edge in neighbors:
                if edge < edge_prime:
                    v1, v2, edge_prime = i, v, edge

        return v1, v2, edge_prime

    n = len(G)
    v1,v2,edge = find_smallest_edge(G)
    Included = [False for _ in range(n)]
    All_Included = n
    mst_sum = 0
    Q = PriorityQueue() # Dodaje do niej krotki typu (edge,next_vertex) gdzie next_vertex to najbliższy sąsiad MST

    # Dodaje pierwszą krawędz
    Included[v1], Included[v2] = True, True
    mst_sum += edge
    for somsiad,soms_edge in G[v1]:
        Q.put([soms_edge,somsiad])


    # while All_Included > 0:



    return



G = [ [(1,3), (2,1), (4,2)], # 0
[(0,3), (2,5) ], # 1
[(1,5), (0,1), (3,6)], # 2
[(2,6), (4,4) ], # 3
[(3,4), (0,2) ] ] # 4
print(beautree(G))


G_kraw = [[0,1,1],[1,3,2],[0,2,3],[1,4,4],[2,3,1],[3,5,1],[4,5,3],[2,4,2]]

def wypisz_kolejke(q):
    # Tworzymy pustą listę do przechowywania elementów kolejki
    elements = []

    # Pobieramy i dodajemy elementy kolejki do listy zgodnie z ich priorytetami
    while not q.empty():
        item = q.get()
        elements.append(item)
        print(item)

    # Ponownie umieszczamy elementy w kolejce
    for item in elements:
        q.put(item)

def prime_MST(G,v_start):
    from queue import PriorityQueue
    def sonsiedztwo_vertexes(L):

        # Licze wierzchołki
        vertx_amount = 0
        for i in L:
            if i[0] > vertx_amount:
                vertx_amount = i[0]
            if i[1] > vertx_amount:
                vertx_amount = i[1]
        vertx_amount += 1

        # Tworze tablice sonsiedztwa
        tablica_sonsiedztwa = [[] for _ in range(vertx_amount)]
        for i in L:
            tablica_sonsiedztwa[i[0]].append([i[1], i[2]])
            tablica_sonsiedztwa[i[1]].append([i[0], i[2]])

        return tablica_sonsiedztwa, vertx_amount

    Q = PriorityQueue()
    G_sons, n = sonsiedztwo_vertexes(G)
    distances = [float('inf') for _ in range(n)]
    been_here = [False for _ in range(n)]
    child = [None for _ in range(n)]

    # Ustawienie pierwszego wierzchołka
    distances[v_start] = 0
    been_here[v_start] = True
    Q.put([v_start, 0])

    # Tutaj mamy basicowa pentelke
    while not Q.empty():

        curr_dist, v = Q.get()
        been_here[v] = True

        for next_v, edge_weight in G_sons[v]:

            # Tutaj musi nastąpić relaxacja dla każdej krawędzi
            if distances[next_v] > edge_weight and been_here[next_v] == False:
                distances[next_v] = edge_weight
                child[next_v] = v

            # Po skonczonej relaxacji kazdej kraw trza dodac wierzcholki do kolejki
                Q.put([edge_weight,next_v])

    return child

print(prime_MST(G_kraw,0))
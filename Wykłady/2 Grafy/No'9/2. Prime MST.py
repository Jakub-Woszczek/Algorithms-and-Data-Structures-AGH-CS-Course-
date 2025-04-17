from queue import PriorityQueue

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
    Q.put([v_start,0])
    distances = [float('inf') for _ in range(n)]
    been_here = [False for _ in range(n)]
    child = [None for _ in range(n)]
    distances[v_start] = 0
    been_here[v_start] = True


    while not Q.empty():
        print('in')
        wypisz_kolejke(Q)

        dist, v = Q.get()
        # Q.queue.clear()
        been_here[v] = True

        for next_v, weight   in G_sons[v]:

            # if been_here[next_v] == False:
            if distances[next_v] > weight:
                distances[next_v] = weight
                child[next_v] = v

            Q.put([weight, next_v])


        print('out')
        wypisz_kolejke(Q)
        print('')

    return child

print(prime_MST(G_kraw,0))

def warrior(G, s, t):
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

    G_sons, n = sonsiedztwo_vertexes(G)
    been_here = [False for _ in range(n)]
    DQ = [[None for _ in range(n)] for _ in range(17)]

    DQ[0][0] = 0

    Q = PriorityQueue()

    queue_val = 1
    Q.put([0, s])  # Robie seeda BFS

    while not Q.empty():
        curr_v = Q.get()[1]
        been_here[curr_v] = True
        curr_tiredness = DQ

        for somsiad,edge in  G_sons[curr_v]:
            if been_here[somsiad] == False:

                # Rozpatruje krok
                D

    return
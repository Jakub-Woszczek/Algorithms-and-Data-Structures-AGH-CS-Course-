L = [[0,1],[0,2],[2,3],[1,4],[3,4],[4,5],[2,5],[5,6],[6,7]]

def DFS_czasy_przetworzenia(G):

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
            tablica_sonsiedztwa[i[0]].append(i[1])
            tablica_sonsiedztwa[i[1]].append(i[0])

        return tablica_sonsiedztwa, vertx_amount

    L_sons, vertx_amnt = sonsiedztwo_vertexes(G)

    def DFS(L_sons,org):
        nonlocal curr_time

        curr_time += 1
        been_here[org] = True
        for next_vertx in L_sons[org]:
            if been_here[next_vertx] == False:
                parent[next_vertx] = org
                DFS(L_sons,next_vertx)

        curr_time += 1
        czasy_przetw[org] = curr_time

    been_here = [False for _ in range(vertx_amnt)]
    parent = [None for _ in range(vertx_amnt)]
    czasy_przetw = [None for  _ in range(vertx_amnt)]

    curr_time = 0

    for i in range(vertx_amnt):
        if been_here[i] == False:
            DFS(L_sons,i)


    # Teraz jeszcze naprawie czasy na normalne
    n = len(czasy_przetw)
    for i in range(len(czasy_przetw)):
        czasy_przetw[i] -= n

    return parent,czasy_przetw


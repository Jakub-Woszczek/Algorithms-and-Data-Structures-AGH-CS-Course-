L = [[0,1],[0,2],[2,3],[1,4],[3,4],[4,5],[2,5],[5,6],[6,7]]
from queue import Queue
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

    return tablica_sonsiedztwa,vertx_amount

def BFS(T_krawendzie,origin):
    Q = Queue()

    T_sonsie, ver_amnt = sonsiedztwo_vertexes(T_krawendzie)
    arr_distances = [-1 for _ in range(ver_amnt)]
    been_here = [False for _ in range(ver_amnt)]
    parent = [None for _ in range(ver_amnt)]


    arr_distances[origin] = 0
    been_here[origin] = True
    Q.put(origin)

    while not Q.empty():
        org = Q.get()
        print(org)
        for v_next in T_sonsie[org]:
            if been_here[v_next] == False:
                been_here[v_next] = True
                arr_distances[v_next] = arr_distances[org] + 1
                parent[v_next] = org
                Q.put(v_next)

    return parent,arr_distances

print(BFS(L,0))
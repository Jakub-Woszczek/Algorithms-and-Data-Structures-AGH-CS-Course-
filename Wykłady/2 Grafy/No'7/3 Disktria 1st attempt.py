G = [[0,1,1],[0,3,2],[1,2,3],[1,4,2],[4,5,5],[2,5,2],[3,2,1],[2,6,3],[3,7,7],[6,7,1],[6,8,8],[7,8,4],[5,8,1]]

L_kraw = [
[[1, 1], [3, 2]],
[[0, 1], [2, 3], [4, 2]],
[[1, 3], [5, 2], [3, 1], [6, 3]],
[[0, 2], [2, 1], [7, 7]],
[[1, 2], [5, 5]],
[[4, 5], [2, 2], [8, 1]],
[[2, 3], [7, 1], [8, 8]],
[[3, 7], [6, 1], [8, 4]],
[[6, 8], [7, 4], [5, 1]],
]
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
        tablica_sonsiedztwa[i[0]].append([i[1],i[2]])
        tablica_sonsiedztwa[i[1]].append([i[0],i[2]])

    return tablica_sonsiedztwa,vertx_amount

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

def disktria_z_G_kraw(G,start,meta):

    from queue import PriorityQueue
    G_kraw, vertex_amnt = sonsiedztwo_vertexes(G)

    # Zrobie tablice dystansów, kolejke, i parentów
    proxi_distances = [float('inf') for _ in range(vertex_amnt)]
    Q = PriorityQueue()
    paretns = [None for _ in range(vertex_amnt)]
    been_here = [False for _ in range(vertex_amnt)]


    # Robimy set pierwszego wierzchołka
    proxi_distances[start] = 0
    Q.put([proxi_distances[start],start])
    been_here[start] = True

    # Teraz trzeba zrobić główną pętlekę
    while not Q.empty():

        # wypisz_kolejke(Q)

        v = Q.get()
        curr_dist,curr_vertx = v[0],v[1]

        # Sprawdzam czy dojechałem do końca
        if curr_vertx == meta:
            return proxi_distances[curr_vertx],paretns

        # Przechodzę do następnych krawędzi
        for somsiad in range(len(G_kraw[curr_vertx])):

            next_vertex,edge_weight = G_kraw[curr_vertx][somsiad][0],G_kraw[curr_vertx][somsiad][1]

            # Trzeba sprawdzić czy tam nie byłem
            if been_here[next_vertex] == False:



                    # Teraz trza zrobić relaxamcje
                if proxi_distances[next_vertex] > proxi_distances[curr_vertx] + edge_weight:
                    proxi_distances[next_vertex] = proxi_distances[curr_vertx] + edge_weight
                    paretns[next_vertex] = curr_vertx
                    Q.put([proxi_distances[next_vertex], next_vertex])


# for i in range(1,9):
#     print(f'z 0 do {i} jest daleko: {disktria_z_G_kraw(G,0,i)}')
# print(disktria_z_G_kraw(G,0,2))
print(disktria_z_G_kraw(G,0,8))
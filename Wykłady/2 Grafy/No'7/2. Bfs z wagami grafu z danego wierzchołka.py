L = [[0,1],[0,2],[2,3],[1,4],[3,4],[4,5],[2,5],[5,6],[6,7]]
L_2 = [[0,1,2],[0,2,4],[1,2,1],[1,3,4],[2,3,2],[2,4,1],[3,5,1],[4,5,3]]
from queue import PriorityQueue
import time
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
print(sonsiedztwo_vertexes(L_2))
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


def BFS(T_krawendzie):
    Q = PriorityQueue()

    T_sonsie, ver_amnt = sonsiedztwo_vertexes(T_krawendzie) # Wierzchołek: [dystans,index]
    arr_distances = [-1 for _ in range(ver_amnt)]
    been_here = [False for _ in range(ver_amnt)]
    parent = [None for _ in range(ver_amnt)]
    distance_iter = 0

    origin = [0,0]
    arr_distances[origin[0]] = 0
    been_here[origin[0]] = True
    Q.put(origin)

    while not Q.empty():
        wypisz_kolejke(Q)
        print(arr_distances)
        vertex = Q.get()
        # print(vertex)
        # Rozwarzam że dystans zmiejszyłem już gdzieś do 0
        if vertex[0] == 0:
            for v_next in T_sonsie[vertex[0]]:
                if been_here[v_next[1]] == False:

                    been_here[vertex[1]] = True
                    print(f'dis_i {distance_iter}')
                    arr_distances[vertex[1]] = distance_iter
                    parent[v_next[1]] = vertex
                    Q.put(v_next)

        else:
            # Trza go włożyć spowrotem
            Q.put(vertex)

            # size_of_q = Q.qsize()


            # Tutaj zmiejszam priorytet każdej o 1, i dystans zwiększam o 1
            size=Q.qsize()
            temp = []
            while size > 0:
                # print(size)
                v = Q.get()
                print(f'usuwam z {v}')
                temp.append([v[0]-1,v[1]])
                size -= 1
                distance_iter += 1

            for v in temp:
                Q.put(v)

        # time.sleep(1)
        print('')




    # while not Q.empty():
    #     org = Q.get()
    #     print(org)
    #     for v_next in T_sonsie[org]:
    #         if been_here[v_next] == False:
    #             been_here[v_next] = True
    #             arr_distances[v_next] = arr_distances[org] + 1
    #             parent[v_next] = org
    #             Q.put(v_next)

    return parent,arr_distances

print(BFS(L_2))
# print(sonsiedztwo_vertexes(L_2))
import time

L_2 = [[0,1,2],[0,2,4],[1,2,1],[1,3,4],[2,3,2],[2,4,1],[3,5,1],[4,5,3]]
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
        tablica_sonsiedztwa[i[0]].append([i[1],i[2]])
        tablica_sonsiedztwa[i[1]].append([i[0],i[2]])

    return tablica_sonsiedztwa,vertx_amount

print(sonsiedztwo_vertexes(L_2)) # T = [index: [ [next_index, odleglosc],..

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

def BFS_weights(T_krawędzie):

    # Stworze arr_sytansow, been here, parenta, distans iter, i T_sonsie
    T_sonsie, ver_amnt = sonsiedztwo_vertexes(T_krawędzie)
    arr_distances = [float('inf') for _ in range(ver_amnt)]
    been_here = [False for _ in range(ver_amnt)]
    parent = [None for _ in range(ver_amnt)]
    distance_iter = 0
    Q = PriorityQueue()

    # Narazie robie seeda na pierwszy wierzchołek

    origin = [0,0]
    Q.put(origin)

    while not Q.empty():
        wypisz_kolejke(Q)
        print(arr_distances)
        vertex_test = Q.get()
        print('')

        # Sprawdzam czy się dystans gdzieś nie skończył
        if vertex_test[1] == 0:

            # Tutaj zaznacze że  byłem tu
            been_here[vertex_test[0]] = True
            arr_distances[vertex_test[0]] = min(distance_iter,arr_distances[vertex_test[0]])

            for next_vertex in T_sonsie[vertex_test[0]]:
                if been_here[next_vertex[0]] == False:
                    parent[next_vertex[0]] = vertex_test[0]
                    print(f'dodaje {next_vertex}')
                    Q.put(next_vertex)

        # Nie skończył się
        else:
            Q.put(vertex_test)

            # Tutaj zmiejszam priorytet każdej o 1, i dystans zwiększam o 1
            size = Q.qsize()
            temp = []
            while size > 0:
                # print(size)
                v = Q.get()
                temp.append([v[0], v[1] - 1])
                size -= 1
            distance_iter += 1

            for v in temp:
                Q.put(v)

        time.sleep(1)

    return arr_distances

print(BFS_weights(L_2))


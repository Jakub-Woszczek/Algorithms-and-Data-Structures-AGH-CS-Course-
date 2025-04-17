G = [ (1,5,10), (4,6,12), (3,2,8),
(2,4,4) , (2,0,10), (1,4,5),
(1,0,6) , (5,6,8) , (6,3,9)]
s = 0
t = 6

G_2 = [(0, 4, 11), (0, 7, 5), (1, 4, 14), (1, 5, 6), (1, 7, 16), (1, 8, 10), (1, 9, 16), (2, 3, 8), (2, 6, 15), (2, 8, 15), (3, 8, 11), (4, 5, 15), (4, 7, 6), (5, 8, 15), (5, 9, 10), (6, 8, 15)]


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

def warrior(G,s,t):
    # Na początku zrobie liste sąsiedztwa

    # Dikstria

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

    def Dikstria_z_przystankami(G_kraw,start,meta):

        from queue import PriorityQueue

        G_sons, v_amnt = sonsiedztwo_vertexes(G_kraw)

        # teraz trzeba stworzyć priority queue,
        Q = PriorityQueue()
        timeings = [float('inf') for _ in range(v_amnt)]
        been_here = [False for _ in range(v_amnt)]

        # Trzeba dodać pierwszy wierzchołek, !!!!!!!! Kolejka w postaci: [timeing,vertex,curr_exhaust]
        timeings[start] = 0
        Q.put([timeings[start],start,0])


        # Teraz basicowa pętelka
        while not Q.empty():



            v = Q.get()
            curr_distance, curr_vertex, curr_tiredness = v[0],v[1],v[2]
            print(f' w wierzchołku {curr_vertex}, tim: {timeings}')

            if curr_tiredness >16:
                timeings[curr_vertex] += 8
                curr_distance += 8
                curr_tiredness = 0

            # Tutaj sprawdzam czy doszedł do celu
            if curr_vertex == meta:
                return timeings[curr_vertex]

            for i in range(len(G_sons[curr_vertex])):

                next_vertex, edge_weight = G_sons[curr_vertex][i][0],G_sons[curr_vertex][i][1]

                if been_here[next_vertex] == False:

                    # Teraz trza by zrobić relaxamcje i ją podziele na 2




                    if timeings[next_vertex] > timeings[curr_vertex] + edge_weight:
                        timeings[next_vertex] = timeings[curr_vertex] + edge_weight


                        Q.put([timeings[next_vertex], next_vertex, curr_tiredness + edge_weight])

                    # else:
                    #
                    #     # Tutaj chyba dodam przystanek
                    #
                    #
                    #     # I robie to samo
                    #     if timeings[next_vertex] > timeings[curr_vertex] + edge_weight + 8:
                    #         timeings[next_vertex] = timeings[curr_vertex] + edge_weight + 8
                    #         # timeings[curr_vertex] += 8
                    #         Q.put([timeings[next_vertex], next_vertex, 0])



    return Dikstria_z_przystankami(G,s,t)

print(warrior(G_2,s,t))

# prawidłowy 70
# 0 -> 6
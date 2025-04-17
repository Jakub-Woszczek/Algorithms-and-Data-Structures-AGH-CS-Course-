def spacetravel( n, E, S, a, b ):
    # n - ilość wierzchołków
    # E - krawędzie z wagami E = [(0, 1, 5) - od v0 do v1 czas 5 ...
    # S - lista osobliwości - S = [0,2,3]
    # a, b - start, meta

    # Zaimportuje kolejke priorytetową
    from queue import PriorityQueue

    # Wygląda na to że przyda się lista sąsiedztwa, i jest basicowa działczy (*≧︶≦))(￣▽￣* )ゞ
    L = [[] for _ in range(n)]
    for i in E:
        L[i[0]].append([i[1], i[2]])
        L[i[1]].append([i[0], i[2]])

    # Zrobie cykl z osobliwości
    L[0].append([S[len(S)-1],0])
    L[len(S)-1].append([S[0], 0])
    for i in range(len(S) - 1):
        j = i + 1
        L[S[i]].append([S[j],0])
        L[S[j]].append([S[i],0])

    # Do dijkstry się przyda array of distances to evaluate in every iteration distance to ceritan vertex
    distances = [float('inf') for _ in range(n)]

    # Traz napisz DiCkstrije w osobnej funkcji
    def dikstria(G, start, destiny, distance):  # NWM w jakiej formie ma być G (´･ω･`)?

        # We evaluate 1st vertes and label it with  distance 0
        distance[start] = 0
        queue = PriorityQueue()  # do kolejki będziemy dodawać tuple (dystans, index_wierzchołka)
        # Dodajemy pierwszego tupla
        queue.put((0, start))
        # Dodaj zmienną arrival żeby zreturnować None jakby nie dojechał
        arrival = 0
        # Tutaj waruna daje dopóki jest jakaś kolejka
        while not queue.empty():

            # Ściągamy górny wierzchołek z niej i idziemy do jego somsiadów ( tutaj mamy index)
            v = queue.get()[1]
            for i in G[v]:  # Tutaj na tablicy sąsiedztwa idę do sąsiadów i=[index_somsiada, dystans]
                v_next = i[0]
                distance_next = i[1]

                # Tu sprawdzę czy arrival siądzie
                if v_next == destiny:
                    arrival = 1
                # Tutaj sprawdzam czy nowy dystans nie jest lepszy
                # print(distance[v_next], distance[v], distance_next)
                if distance[v_next] > distance[v] + distance_next:
                    distance[v_next] = distance[v] + distance_next
                    queue.put((distance[v_next], v_next))

        # Sprawdzę czy wgl doszło
        if arrival == 0:
            return None
        return distance[destiny]

    return dikstria(L, a, b, distances)


E = [(0,1, 5),
(1,2,21),
(1,3, 1),
(2,4, 7),
(3,4,13),
(3,5,16),
(4,6, 4),
(5,6, 1)]
S = [ 0, 2, 3 ]
a = 1
b = 5
n = 7

print(spacetravel(n,E,S,a,b))
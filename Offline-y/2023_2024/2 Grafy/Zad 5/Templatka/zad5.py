# Jakub Woszczek

# Połączyłem osobliwości cyklem krórego krawędzie mają wagę 0
# i szukałem drogi z najmniejszą wagą za pomocą algorytmy Dikstry
# ( bardziej szczegółowy opis w kodzie)

# Szacuje złożoność na O(ElogV + E) - Dikstra i stowrzenie listy sąsiedztwa

from zad5testy import runtests

def spacetravel( n, E, S, a, b ):

    from queue import PriorityQueue

    # Wygląda na to że przyda się lista sąsiedztwa
    L = [[] for _ in range(n)]
    for i in E:
        L[i[0]].append([i[1], i[2]])
        L[i[1]].append([i[0], i[2]])

    # Zrobie cykl z osobliwości
    L[0].append([S[len(S) - 1], 0])
    L[len(S) - 1].append([S[0], 0])
    for i in range(len(S) - 1):
        j = i + 1
        L[S[i]].append([S[j], 0])
        L[S[j]].append([S[i], 0])

    # Do dijkstry się przyda array of distances to evaluate in every iteration distance to ceritan vertex
    distances = [float('inf') for _ in range(n)]

    # DiCkstrije w osobnej funkcji
    def dikstria(G, start, destiny, distance):

        # Daje dystans początkowego wierzchołka jako 0
        distance[start] = 0
        queue = PriorityQueue()  # do kolejki będziemy dodawać tuple (dystans, index_wierzchołka)
        # Dodajemy pierwszy wierzchołek
        queue.put((0, start))

        # Jeżeli się pojawi wierzchołek do którego chce dojść to arrival=1, inaczer return None
        arrival = 0

        # Tutaj daje waruna daje dopóki jest jakaś kolejka
        while not queue.empty():

            # Ściągamy górny wierzchołek z niej i idziemy do jego somsiadów ( v to index)
            v = queue.get()[1]
            for i in G[v]:  # Tutaj na tablicy sąsiedztwa idę do sąsiadów i=[index_somsiada, dystans]
                v_next = i[0]
                distance_next = i[1]

                # Tu sprawdzam czy będe tam gdzie chce
                if v_next == destiny:
                    arrival = 1

                # Tutaj sprawdzam czy nowy dystans nie jest lepszy
                if distance[v_next] > distance[v] + distance_next:
                    distance[v_next] = distance[v] + distance_next
                    queue.put((distance[v_next], v_next))

        # Sprawdzę czy osiągnąłem destiny
        if arrival == 0:
            return None
        return distance[destiny]

    return dikstria(L, a, b, distances)
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
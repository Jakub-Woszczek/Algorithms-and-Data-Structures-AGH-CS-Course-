def gold( G,V,s,t,r ):
    from queue import PriorityQueue

    # Plen dzizłania do Dikstra z pomininiemciem rabowania zamku
    # Później wszystkie najktótsza ścieżki z startu do każdego zamku i później zmodyfikowane ścieżki do każdego innego zamku

    # Dikstria
    n = len(G)
    distances = [float('inf') for _ in range(n)]

    def dikstria_s(G,org):

        been_here = [False for _ in range(n)]

        distances[org] = 0
        Q = PriorityQueue()

        Q.put([0,org]) # W kolejce będą krotki [val_wierzchołka,wierzchołek]

        while not Q.empty():

            curr_weight, curr_vertx = Q.get()
            been_here[curr_vertx] = True

            for somsiad, edge in G[curr_vertx]:
                distances[somsiad] = min(distances[somsiad],curr_weight + edge)
                if been_here[somsiad] == False:
                    Q.put([distances[somsiad],somsiad])


    dikstria_s(G,s)
    distances_no_qonquest = distances[t]
    conquest_distances = [float('inf') for _ in range(n)]

    def dikstria_with_conquest(G,org,r):

        been_here = [False for _ in range(n)]

        conquest_distances[org] = 0
        Q = PriorityQueue()

        Q.put([0, org])  # W kolejce będą krotki [val_wierzchołka,wierzchołek]

        while not Q.empty():

            curr_weight, curr_vertx = Q.get()
            been_here[curr_vertx] = True

            for somsiad, edge in G[curr_vertx]:
                conquest_distances[somsiad] = min(conquest_distances[somsiad], curr_weight + edge*2+r)
                if been_here[somsiad] == False:
                    Q.put([conquest_distances[somsiad], somsiad])

    dikstria_with_conquest(G,t,r)

    min_conquest = float('inf')
    for v_conquer in range(n):
        to_castle = distances[v_conquer]
        from_castle = conquest_distances[v_conquer] - V[v_conquer]

        min_conquest = min(min_conquest,to_castle + from_castle)

    return min_conquest


    # print(dikstria_with_conquest(G,0,6,7))




G = [[(1,9), (2,2)], # 0
[(0,9), (3,2), (4,6)], # 1
[(0,2), (3,7), (5,1)], # 2
[(1,2), (2,7), (4,2), (5,3)], # 3
[(1,6), (3,2), (6,1)], # 4
[(2,1), (3,3), (6,8)], # 5
[(4,1), (5,8)] ] # 6
V = [25,30,20,15,5,10,0]
s = 0
t = 6
r = 7
print(gold(G,V,s,t,r))
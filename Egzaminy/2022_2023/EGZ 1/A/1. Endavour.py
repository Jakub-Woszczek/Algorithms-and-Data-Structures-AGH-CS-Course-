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


    def dikstria_with_conquest(G,start,meta,r):

        Q = PriorityQueue()
        been_here = [False for _ in range(n)]

        Q.put([0,start])
        been_here[start]=  True
        distances = [float('inf') for _ in range(n)]

        while not Q.empty():
            curr_distans, curr_v = Q.get()
            # print(f'jestem w {curr_v} i dystans to {curr_distans}')
            been_here[curr_v] = True

            if curr_v == meta:
                # distances[curr_v]=  curr_distans
                return distances[meta]

            for somsiad,edge in G[curr_v]:

                distans = curr_distans + edge*2 + r
                distances[somsiad] = min(distances[somsiad],distans)

                if been_here[somsiad] == False:
                    Q.put([distans,somsiad])

        return distances[meta]

    min_conquest = float('inf')
    for v_conquer in range(n-1):
        to_castle = distances[v_conquer]
        from_castle = dikstria_with_conquest(G,v_conquer,t,r) - V[v_conquer]

        min_conquest = min(min_conquest,to_castle + from_castle)

    return min(distances_no_qonquest,min_conquest)



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
# print()gold(G,V,s,t,r))
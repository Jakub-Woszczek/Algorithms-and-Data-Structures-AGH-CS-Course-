def tory_amos(E,A,B):

    from queue import PriorityQueue
    max_v = 0
    for x, y, dist, typ in E:
        max_v = max(max_v, x, y)

    G_sons = [[] for _ in range(max_v + 1)]
    Distances_arr_I = [float('inf') for _ in range(max_v + 1)]
    Distances_arr_P = [float('inf') for _ in range(max_v + 1)]
    been_here = [False for _ in range(max_v + 1)]
    Q = PriorityQueue()  # (Dist, somsiad, typ)

    for x, y, dist, typ in E:
        G_sons[x].append([y, dist, typ])
        G_sons[y].append([x, dist, typ])

    been_here[A] = True
    Distances_arr_I[A],Distances_arr_P[A] = 0, 0
    for somsiad,edge,typ in G_sons[A]:
        Q.put([edge, somsiad, typ])
        if typ == 'I':
            Distances_arr_I[somsiad] = edge
        else:
            Distances_arr_P[somsiad] = edge


    while not Q.empty():

        curr_dist,curr_v,tory_prev=  Q.get()
        been_here[curr_v] = True

        if curr_v == B:
            return curr_dist

        for somsiad,edge,tory in G_sons[curr_v]:

            # Aktualizacja wierzchołków
            if tory != tory_prev:
                if tory == 'I':
                    Distances_arr_I[somsiad] = min(Distances_arr_I[somsiad],curr_dist + 20 + edge)
                else:
                    Distances_arr_P[somsiad] = min(Distances_arr_P[somsiad], curr_dist + 20 + edge)

            else:
                if tory == 'I':
                    Distances_arr_I[somsiad] = min(Distances_arr_I[somsiad], curr_dist + 5 + edge)

                else:
                    Distances_arr_P[somsiad] = min(Distances_arr_P[somsiad], curr_dist + 10 + edge)

            if been_here[somsiad] == False:

                if tory == 'I': Q.put([Distances_arr_I[somsiad],somsiad,tory])
                else: Q.put([Distances_arr_P[somsiad],somsiad,tory])


    return min(Distances_arr_P[B],Distances_arr_I[B])

E = [(0, 1, 5, 'P'), (1, 3, 1, 'I'), (3, 4, 1, 'I'), (2, 4, 1, 'P'), (2, 5, 1, 'I'), (0, 5, 5, 'P')]
A = 5
B = 3
print(tory_amos(E,A,B))
def islands(G, A, B):
    from queue import PriorityQueue
    def from_matrix_to_G_sons(M):
        n = len(M)
        G_sons = [[] for _ in range(n)]

        for row in range(0, n):
            for col in range(row + 1, n):
                if M[row][col] != 0:
                    G_sons[row].append((col, M[row][col]))
                    G_sons[col].append((row, M[row][col]))

        return G_sons

    n = len(G)
    G_sons = from_matrix_to_G_sons(G)
    been_here = [False for _ in range(n)]
    Q =  PriorityQueue() # Kroteczka (curr_dist,last_edge,curr_v)



    for somsiad,waga in G_sons[A]:
        Q.put((waga,waga,somsiad))
    been_here[A] = True

    while not Q.empty():

        distance,last_edge,vertex = Q.get()

        if vertex == B:
            return distance

        for somsiad,waga in G_sons[vertex]:

            if been_here[somsiad] == False and waga != last_edge:

                Q.put((distance + waga,waga,somsiad))
                been_here[somsiad] = True


    return None




G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]

print(islands(G1,5,2))
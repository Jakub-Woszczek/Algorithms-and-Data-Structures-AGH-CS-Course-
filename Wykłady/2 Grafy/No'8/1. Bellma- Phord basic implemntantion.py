G = [[0,1,-3],[1,2,-5],[2,3,3],[4,3,-1],[3,5,5],[5,4,-3],[5,1,4],[5,6,-1],[6,1,2]]

def Belliman_phord(G_kraw):

    # Ilość krawędzi
    vertex_amnt = 0
    for i in G_kraw:
        if i[0] > vertex_amnt:
            vertex_amnt = i[0]
        elif i[1] > vertex_amnt:
            vertex_amnt = i[1]
    vertex_amnt += 1

    # Robie set parenta i distances
    parent = [None for _ in range(vertex_amnt)]
    distances = [float('inf') for _ in range(vertex_amnt)]

    # Ustawiam pierwszą odległość na 0 bruh
    distances[0] = 0

    # Teramz robimy relaxamcje

    for _ in range(vertex_amnt-1):
        for edge in G_kraw:
            curr_v = edge[0]
            next_v = edge[1]
            edge_weight = edge[2]

            # Teraz namstępuje relaxamcja
            distances[next_v] = min(distances[next_v],distances[curr_v] + edge_weight)

    # Teraz werymfikacja
    for edge in G_kraw:
        curr_v = edge[0]
        next_v = edge[1]
        edge_weight = edge[2]

        # if distances[curr_v] != float('inf') and distances[next_v] > distances[curr_v] + edge_weight:
        if distances[next_v] > distances[curr_v] + edge_weight:
            return True

    return distances

print(Belliman_phord(G))
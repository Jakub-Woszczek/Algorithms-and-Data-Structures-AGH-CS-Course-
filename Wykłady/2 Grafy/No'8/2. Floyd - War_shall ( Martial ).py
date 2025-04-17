G = [[0,1,4],[1,2,2],[2,3,5],[2,4,4],[4,1,-3],[3,4,-1],[3,4,-1],[4,5,1],[3,5,3],[5,6,8]]

def Flood_Martial(G_kraw):

    # Ilość krawędzi
    vertex_amnt = 0
    for i in G_kraw:
        if i[0] > vertex_amnt:
            vertex_amnt = i[0]
        elif i[1] > vertex_amnt:
            vertex_amnt = i[1]
    vertex_amnt += 1

    Matrix_odleglosci = [[float('inf') for _ in range(vertex_amnt)] for _ in range(vertex_amnt)]

    # Do siebie wierchołki
    for i in range(vertex_amnt):
        Matrix_odleglosci[i][i] = 0

    # Zaznaczam krawędzie
    for edge in G:
        Matrix_odleglosci[edge[0]][edge[1]] = edge[2]

    # Lecymy V^3 §(*￣▽￣*)§

    for i in range(vertex_amnt):
        for j in range(vertex_amnt):
            for k in range(vertex_amnt):

                Matrix_odleglosci[j][k] = min(Matrix_odleglosci[j][k],
                                          Matrix_odleglosci[j][i] + Matrix_odleglosci[i][k])


    return Matrix_odleglosci

T = Flood_Martial(G)

for bruh in T:
    print(bruh)




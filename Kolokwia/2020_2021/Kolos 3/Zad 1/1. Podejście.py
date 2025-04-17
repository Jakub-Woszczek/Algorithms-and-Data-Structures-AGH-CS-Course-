def Floyd_Matial(Matrix_wierzcholkow): # Przyjmuje matrixa z wagami krawedzi (do siebie jest 0)

    # Ilość krawędzi
    vertex_amnt = len(Matrix_wierzcholkow)

    # Przygotowanie Matrixa
    Matrix_odleglosci = [[float('inf')] * vertex_amnt for _ in range(vertex_amnt)]

    for i in range(vertex_amnt):
        for j in range(vertex_amnt):
            if i == j:
                Matrix_odleglosci[i][j] = 0
            elif Matrix_wierzcholkow[i][j] != 0:
                Matrix_odleglosci[i][j] = Matrix_wierzcholkow[i][j]
    for bruh in Matrix_odleglosci:
        print(bruh)

    # Lecymy V^3 §(*￣▽￣*)§
    for i in range(vertex_amnt):
        for j in range(vertex_amnt):
            for k in range(vertex_amnt):
                Matrix_odleglosci[j][k] = min(Matrix_odleglosci[j][k],
                                        Matrix_odleglosci[j][i] + Matrix_odleglosci[i][k])

    return Matrix_odleglosci # Returnuje talblice min odleglosci z każdego wieszcholka do innego ( do siebie jest 0 )

def T_possible_double_v(T_dist,d_min):
    n = len(T_dist)
    T_keep_dist = [[False for _ in range(len(n))] for _ in range(len(n))]

    for i in range(n):
        for j in range(n):
            if T_dist[i][j] >= d_min:
                T_dist[i][j] = True

    return T_keep_dist

def T_sons_z_matrix_wag(Matrix_wag):
    n = len(Matrix_wag)
    adjacency_list = [[] for _ in range(n)]

    # Przetworzenie macierzy sąsiedztwa na tablicę sąsiedztwa
    for i in range(n):
        for j in range(n):
            if Matrix_wag[i][j] != 0:  # Jeśli istnieje krawędź (i, j)
                adjacency_list[i].append(j)

    return adjacency_list

def keep_distance(M, x, y, d):
    n = len(M)
    # Tablica odległości każdego weirzchołka do każdego
    M_odleglosci = Floyd_Matial(M)

    # Tablica True/False czy dane wierzcholki są od siebie wystarzczajaco oddalone
    Tablica_mozliwych_dystansow = T_possible_double_v(M_odleglosci,d)

    # Tablica sąsiedztwa
    T_sons = T_sons_z_matrix_wag(M)

    # Potrzebuje tabilicy z put(), z get()
    def put(T,val):
        if val not in T:
            T.append(val)

        return T
    def get(T): # Biore pierwszą wartość
        n = len(T)
        if n > 0:
            val = T[0]
            del T[0]
            return val
        return None

    # Trzeba przygotować BFS z lewej i z prawej
    Fala_X = []
    been_here_X = [False for _ in range(n)]
    Fala_Y = []
    been_here_Y = [False for _ in range(n)]
    vertexes_possible_path = [[] for _ in range(n)]

    # Przygotowanie BFS-ow
    Fala_X.append(x)
    Fala_Y.append(y)
    been_here_X[x],been_here_Y[y] = True,True

    while len(Fala_X) > 0:

        # Przesune Fale X
        for _ in range(len(Fala_X)):
            vertex = get(Fala_X)
            been_here_X[vertex] = True
            for somsiad in T_sons[vertex]:
                if been_here_X[somsiad] == False:
                    put(Fala_X,somsiad)

        # Przesune Fale Y
        for _ in range(len(Fala_Y)):
            vertex = get(Fala_Y)
            been_here_Y[vertex] = True
            for somsiad in T_sons[vertex]:
                if been_here_Y[somsiad] == False:
                    put(Fala_Y,somsiad)

        # Zaznaczam możliwe drogi
        for i in range(len(Fala_X)):
            vertex = Fala_X[i]
            for opposite_vertex in Fala_Y:
                if Tablica_mozliwych_dystansow[vertex][opposite_vertex] == True:
                    vertexes_possible_path[vertex].append(opposite_vertex)


    return vertexes_possible_path






M1 = [ [0, 1, 1, 0, 0, 0],
       [1, 0, 0, 1, 0, 0],
       [1, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 1],
       [0, 0, 1, 0, 0, 1],
       [0, 0, 0, 1, 1, 0]]

# T = Floyd_Matial(M1)
T = T_sons_z_matrix_wag(M1)
for bruh in T:
    print(bruh)
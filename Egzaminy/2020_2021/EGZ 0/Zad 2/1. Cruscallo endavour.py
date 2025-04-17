class Node:
    def __init__(self):
        self.left = None # lewe poddrzewo
        self.leftval = 0 # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None # prawe poddrzewo
        self.rightval = 0 # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None # miejsce na dodatkowe dane

def valuableTree(T, k):
    T_edges = []

    def edges_search(p,index):
        nonlocal T_edges

        if p.left == None and p.right == None:
            return

        if p.left != None:
            T_edges.append([index,2*index+1,p.leftval])
            edges_search(p.left,2*index+1)

        if p.right!= None:
            T_edges.append([index,2*(index+1),p.rightval])
            edges_search(p.left,2*(index+1))

    edges_search(T,0)

    max_vertex = 0
    for x,y,v in T_edges:
        max_vertex = max(x,y,max_vertex)

    T_edges.sort(key=lambda x: x[2])

    vertexes_colurs = [[None] for _ in range(max_vertex+1)]
    edges_colurs = [[None] for _ in range(len(T_edges))]
    color = 0
    ile_dany_kolor_ma_krawędzi = [[] for _ in range(len(T_edges))]
    val_koloru_suma = [[] for _ in range(len(T_edges))]

    i = 0
    for x,y,val in T_edges:

        if edges_colurs[i][0] == None:
            edges_colurs[i][0] = color
        else:
            edges_colurs[i].append(color)

        if vertexes_colurs[x][0] == None:
            vertexes_colurs[x][0] = color
        else:
            vertexes_colurs[x].append(color)

        if vertexes_colurs[y][0] == None:
            vertexes_colurs[y][0] = color
        else:
            vertexes_colurs[y].append(color)

        i += 1


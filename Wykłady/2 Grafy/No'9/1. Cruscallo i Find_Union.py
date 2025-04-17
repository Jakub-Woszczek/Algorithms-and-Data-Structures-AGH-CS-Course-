class Node:
    def __init__(self,value):
        self.val = value
        self.parent = self
        self.rank = 0

G_kraw = [[0, 1, 15], [0, 2, 5], [0, 3, 10], [1, 2, 8], [1, 4, 5], [1, 5, 12], [2, 3, 5], [2, 4, 6], [3, 4, 2], [3, 5, 11], [4, 5, 2]]


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):

    x = find(x)
    y = find(y)

    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

sorted_edges = [[3, 4, 2], [4, 5, 2], [0, 2, 5], [1, 4, 5], [2, 3, 5], [2, 4, 6], [1, 2, 8], [0, 3, 10], [3, 5, 11], [1, 5, 12], [0, 1, 15]]

def kruskal(n, edges):
    # Tworzenie wierzchołków
    nodes = [Node(i) for i in range(n)]

    # Sortowanie krawędzi według wagi
    edges = sorted(edges, key=lambda x: x[2])
    print(edges)
    mst = []

    for u, v, weight in edges:
        node_u = nodes[u]
        node_v = nodes[v]

        if find(node_u) != find(node_v):
            union(node_u, node_v)
            mst.append((u, v, weight))

    return mst

print(kruskal(6,G_kraw))
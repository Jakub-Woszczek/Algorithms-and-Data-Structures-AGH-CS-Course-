def floyd_warshall(G: 'graph represented by adjacency matrix'):
    n = len(G)
    inf = float('inf')
    W = [[inf] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j]:
                W[i][j] = G[i][j]
            elif i == j:
                W[i][j] = 0

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]

    return W


def create_graph(M, dist, d):
    n = len(M)
    inf = float('inf')
    G = [[[] for _ in range(n)] for _ in range(n)]

    for x1 in range(n):
        for x2 in range(n):
            if x1 != x2 and not M[x1][x2]: # Tutaj sprawdzam czy Karol przechodzi na inny wierzchołek do którego ISTNIEJE krawędź
                print(f'Carol nie ma krawędzi')
                continue
            for y1 in range(n):
                for y2 in range(n):
                    print(f'Położenie Carol   {x1} ---> {x2}   , Maxa V_1   {y1} ----> {y2}  ')
                    if y1 != y2 and not M[y1][y2]: # Tutaj sprawdzam czy Max ma ścieżke z jednego wierzchołka do drugiego i czy to nie są te same
                        print(f'Nie pykło bo Max nie ma krawędzi')
                        continue
                    if (x1 == x2 and y1 == y2): # Tutaj sprawdzam czy przypadkiem Max i Carol nie stoją w miejscu
                        print(f' Stoją sieroty w miejscu')
                        continue
                    if (x2 == y1 and y2 == x1): # Tutaj sprawdzam czy przypadkiem nie przechodzą po jednej krawędzi
                        print(f'Po jednej krawędzi jadą')
                        continue
                    if d <= dist[x2][y2] < inf:
                        G[x1][y1].append((x2, y2))
                        print(f'pykło')
    print('')
    for bruh in G:
        print(bruh)
    return G


def get_path(parents, coords):
    path = []

    while coords:
        path.append(coords)
        u, v = coords
        coords = parents[u][v]

    path.reverse()
    return path


def keep_distance(M, x, y, d):
    dist = floyd_warshall(M)
    G = create_graph(M, dist, d)
    n = len(G)

    visited = [[False] * n for _ in range(n)]
    parents = [[None] * n for _ in range(n)]

    def dfs(u, v):
        visited[u][v] = True
        if u == y and v == x:
            return True
        for u2, v2 in G[u][v]:
            if not visited[u2][v2]:
                parents[u2][v2] = u, v
                if dfs(u2, v2):
                    return True
        return False

    dfs(x, y)

    return get_path(parents, (y, x))

M = [
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 1],
[0, 1, 1, 0]]

keep_distance(M,0,3,2)
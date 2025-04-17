# DAG - acykliczny graf skierowany
# Szukam ścieżki halimtona
def topological_sort(G):
    n = len(G)
    visited = [False]*n
    T = [None]*n
    i = n

    def dfs(u):
        nonlocal i
        visited[u] = True
        for v in G[u]:
            if not visited[u]:
                dfs(v)
        i -=1
        T[i] = u

    for u in range(n):
        if not visited[u]:
            dfs(u)
    return T

def solve(G):
    T = topological_sort(G)
    for i in range(len(T)-1):
        u = T[i]
        Found = False
        for v in G[u]:
            if v == T[i+1]
                Found = True
            if not Found:
                return False

    return True
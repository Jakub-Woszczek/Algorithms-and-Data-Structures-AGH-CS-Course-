def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    disconnected = [False for _ in range(n)]
    order = []
    def visit_DFS(G,w):
        visited[w] = True
        for i in (G[w]):
            if not visited[i]:
                visit_DFS(G,i)

        disconnected[w] = True
        order.append(i)
import queue

def BFS(G):
    q = queue()
    n = len(G)
    visited = [False]*n
    q.append()
    parent=[-1]*n
    while q:
        tmp,d,p = q.pop()
        if d == 0:
            visited[tmp] = True
            if parent[tmp] != -1:
                continue
            parent[tmp] = p
            # for c,d: G[tmp]:
            #     if  not visited[c]:
            #         q.append(c,d-1,tmp)
            # NWM
import queue

def printparent(end,etad,parent):
    if end == etad:
        print(etad)
        return
    printparent(parent[end],etad,parent)
    print(end)
    return

def BFS(G,start,end):
    n = len(G)
    q = queue()
    visited = [False for _ in range(n)]
    # d = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    q.append(parent)
    while len(q) > 0:
        tmp = q.pop()
        visited[tmp] = True
        for i in range(n):
            if G[tmp][i]:
                visited[i] = True
                parent[i] = tmp
                if i == end:
                    printparent(end,parent)
                    return
                q.append(i)
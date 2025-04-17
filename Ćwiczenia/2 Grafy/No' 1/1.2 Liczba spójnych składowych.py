def DFS():
    return

def solve(V):
    spojne = 0
    visited = [False]*len(V)
    for i in range(len(V)):
        if visited[i]:
            continue
        DFS(V,visited,i)
        spojne += 1
    return spojne
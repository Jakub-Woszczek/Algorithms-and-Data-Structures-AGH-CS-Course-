import queue

def solve(arr,n):
    visited = [False]*n
    color = [None]*n
    # 0 kol
    Q = queue()
    Q.push(0)
    while not Q.empty():
        tmp = Q.pop
        for i in arr[tmp]:
            if visited[i] and color[i] == color[tmp]:
                return False
            elif not visited[i]:
                color[i] = 1 - color[tmp]
                Q.append[i]

    return True
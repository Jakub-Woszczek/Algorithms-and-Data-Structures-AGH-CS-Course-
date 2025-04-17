from zad3testy import runtests

    
def tasks(T):
    def G_sons_creator(T):
        n = len(T)
        T_sons = [[] for _ in range(n)]
        for row in range(n):
            for col in range(row + 1, n):
                if T[row][col] == 1:
                    T_sons[row].append(col)
                elif T[row][col] == 2:
                    T_sons[col].append(row)

        return T_sons

    def been_everywhere(T):
        for el in T:
            if el == False:
                return False
        return True

    T_sons = G_sons_creator(T)
    n = len(T)
    been_here = [False for _ in range(n)]
    przetworzone = []

    def dfs(vertex):
        nonlocal przetworzone, been_here, T_sons

        # if len(T_sons[vertex]) == 0:
        #     # przetworzone.append(vertex)
        #     return
        been_here[vertex] = True
        for somsiad in T_sons[vertex]:
            if been_here[somsiad] == False:
                been_here[somsiad] = True
                dfs(somsiad)

        przetworzone.append(vertex)
        return

    i = 0
    while been_everywhere(been_here) == False and i < n:

        if been_here[i] == False:
            dfs(i)

        i += 1

    return przetworzone[::-1]
    return [i for i in range(len(T))]  # domyslny wynik [0,1,2,... ]



runtests( tasks )

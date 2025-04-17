from zad1testy import runtests

def best_root( L ):
    n = len(L)
    been_here = [False for _ in range(n)]
    max_lengt = 0
    right_vertex = None

    def dfs(vertex, lengt):
        nonlocal right_vertex
        print(f'przyjechałem na {vertex}, z dlugoscia {lengt}')
        max_lengt = lengt
        been_here[vertex] = True
        for somsiad in L[vertex]:

            if been_here[somsiad] == False:
                max_lengt = max(dfs(somsiad, lengt + 1), max_lengt)

        print(f'lengt {lengt},max_lengt {max_lengt}, vertex {vertex} ')
        if lengt == (max_lengt / 2) // 1 + 1:
            right_vertex = vertex

        return max(max_lengt, lengt)

    i = 0
    for list in L:
        if len(list) == 1:
            org = i
            break
        i += 1

    dfs(org, 1)
    return right_vertex
    n = len(L)
    return -1


runtests( best_root ) 

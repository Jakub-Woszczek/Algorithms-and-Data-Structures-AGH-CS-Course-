def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)


def projects(n, L):

    def lista_somsiedztwa(n,L):

        List_soms = [[] for i in range(n)]

        for next,first in L:

            List_soms[first].append(next)

        return List_soms
    L_soms = lista_somsiedztwa(n,L)

    been_here = [False for _ in range(n)]
    dfs_timeings = [1 for _ in range(n)]


    def DFS(vertex):
        been_here[vertex] = True
        if len(L_soms[vertex]) == 0:
            dfs_timeings[vertex] = 1

        else:
            max_time = 0
            for somsiad in L_soms[vertex]:
                if been_here[somsiad] == False:
                    max_time = max(max_time,DFS(somsiad))
                else:
                    max_time = max(max_time,dfs_timeings[somsiad])
            dfs_timeings[vertex] = max_time + 1

        return dfs_timeings[vertex]

    max_len = 0
    for v_org in range(n):

        if been_here[v_org] == False:
            max_len = max(max_len,DFS(v_org))



    return max_len

n = 4
L = [(3, 1), (1, 2), (1, 0)]
print(projects(n,L))
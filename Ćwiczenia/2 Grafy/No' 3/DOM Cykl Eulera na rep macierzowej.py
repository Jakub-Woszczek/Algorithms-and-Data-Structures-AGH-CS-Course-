L = [[0,1],[1,5],[2,1],[2,0],[1,4],[4,5],[5,3],[4,3],[4,2],[2,6],[3,6],[5,7],[3,8],[8,7]]


def z_tablicy_krawędzi_do_macierzowej(L):
    # Tworzę matrixa krawędzi
    max_ver = 0
    for i in L:
        if i[0] > max_ver:
            max_ver = i[0]
        if i[1] > max_ver:
            max_ver = i[1]

    matrix = [[0 if i != j else None for i in range(max_ver+1)] for j in range(max_ver+1)]

    # Teraz trzeba pozaznaczać krawędzie
    for i in L:
        matrix[i[0]][i[1]], matrix[i[1]][i[0]] = 1, 1
    return matrix

def cykl_ojlera(L): # Dajmy że przyjmuje tablice jako krawędzie

    matrix = z_tablicy_krawędzi_do_macierzowej(L)
    euler_cycle = []
    n = len(matrix)

    # Jeszcze sie przyda funkcyja która sprawdza czy zostały jejszcze jakiejś krawędzie (xd, wsm to nwm)
    def is_done(matrix):
        for i in  range(len(matrix)):
            for j in range(i+1,len(matrix)):
                if matrix[i][j] == 1:
                    return False
        return True

    def DFS(orgin,matrix):

        # Tutaj mamy waruneczek końcowy
        if is_done(matrix) == True:
            euler_cycle.insert(0,orgin)
            return

        for i in range(n):
            if matrix[orgin][i] == 1:
                matrix[orgin][i],matrix[i][orgin] = 0,0
                DFS(i,matrix)

        euler_cycle.insert(0, orgin)
        return


    # Narazie trzeba ustalić z jakiego wierzchołka zaczynamy
    orgin = 0
    DFS(orgin,matrix)

    return euler_cycle

print(cykl_ojlera(L))
L = [[0,1],[0,2],[2,1,],[2,3],[3,4],[3,5],[4,5],[5,6],[6,8],[8,10],[8,9],[9,7],[6,7],[7,11],[11,12]]
def mosciki(L,org_vertex):
    lista_moscikow = []
    # Na tablice somsiedztwa
    def sonsiedztwo_vertexes(L):

        # Licze wierzchołki
        vertx_amount = 0
        for i in L:
            if i[0] > vertx_amount:
                vertx_amount = i[0]
            if i[1] > vertx_amount:
                vertx_amount = i[1]
        vertx_amount += 1

        # Tworze tablice sonsiedztwa
        tablica_sonsiedztwa = [[] for _ in range(vertx_amount)]
        for i in L:
            tablica_sonsiedztwa[i[0]].append(i[1])
            tablica_sonsiedztwa[i[1]].append(i[0])

        return tablica_sonsiedztwa, vertx_amount

    L_somsiedztwa, vertex_amnt = sonsiedztwo_vertexes(L)

    # Trzeba tablica z czasami odwiedzenia, i lov(), been_here

    arr_czasy_odwiedzenia = [None for _ in range(vertex_amnt)]
    lov = [None for _ in range(vertex_amnt)]
    been_here = [False for _ in range(vertex_amnt)]
    child = [None for _ in range(vertex_amnt)]
    parent = [None for _ in range(vertex_amnt)]

    # Teraz DFS-ik

    def DFS(vertex,curr_time):

        # Zaznaczam lov, been_here, timeing
        lov[vertex] = curr_time
        been_here[vertex] = True
        arr_czasy_odwiedzenia[vertex] = curr_time

        # Ide do somsiadów
        for next_vertex in L_somsiedztwa[vertex]:

            # Jeżeli tam nie byłem: zaznaczam child i parent i ide

            if been_here[next_vertex] == False:
                child[vertex] = next_vertex
                parent[next_vertex] = vertex
                DFS(next_vertex, curr_time + 1)

            # Jeżeli byłem i ten gnoj nie jest parentem

            elif lov[next_vertex] < lov[vertex] and child[next_vertex] != vertex:
                lov[vertex] = lov[next_vertex]

        # Wracając poprawiam lov poprawiam

        if child[vertex] != None and lov[child[vertex]] < lov[vertex]:
            lov[vertex] = lov[child[vertex]]

        # Dajmy że to tutaj trzeba mosty sprawdzać

        if arr_czasy_odwiedzenia[vertex] == lov[vertex] and vertex != org_vertex:
            lista_moscikow.append([vertex,parent[vertex]])

    # Trza jeszcze odpalic DFS
    DFS(org_vertex,1)

    return lista_moscikow, lov, arr_czasy_odwiedzenia


# print(mosciki(L,8))

lista,lov,timeings = mosciki(L,8)
print(lista)
print(lov)
print(timeings)

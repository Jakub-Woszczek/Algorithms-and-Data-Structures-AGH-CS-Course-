L = [[0,1],[2,0],[1,2],[3,4],[5,6],[4,5],[6,3],[9,7],[7,8],[7,10],[10,9],[8,9],[0,10],[2,3],[4,7],[5,9]]
L_2 = [[0,1],[1,2],[0,2],[2,3],[3,0],[5,4],[4,6],[4,8],[7,4],[8,7],[6,7],[6,5],[9,10],[10,11],[11,9],[3,9],[2,4],[1,6],[10,7]]

def lista_silnie_skladowych(L): # L - tablica krawędzi

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

        return tablica_sonsiedztwa, vertx_amount

    # tablica_sons = [[1, 10], [2], [0, 3], [4], [5, 7], [6, 9], [3], [8, 10], [9], [7], [9]]

    def DFS_czasy_przetworzenia(G):

        L_sons, vertx_amnt = sonsiedztwo_vertexes(G)

        def DFS(L_sons, org):
            nonlocal curr_time

            curr_time += 1
            been_here[org] = True
            for next_vertx in L_sons[org]:
                if been_here[next_vertx] == False:
                    parent[next_vertx] = org
                    DFS(L_sons, next_vertx)

            curr_time += 1
            czasy_przetw[org] = curr_time

        been_here = [False for _ in range(vertx_amnt)]
        parent = [None for _ in range(vertx_amnt)]
        czasy_przetw = [None for _ in range(vertx_amnt)]

        curr_time = 0

        for i in range(vertx_amnt):
            if been_here[i] == False:
                DFS(L_sons, i)

        return czasy_przetw, vertx_amnt

    timeings, vertex_amnt = DFS_czasy_przetworzenia(L_2)

    # Tutaj obróce krawędzie i zwróce tablice somsiedztwa
    def rev_edges(L, vertx_amount):

        for i in range(len(L)):
            L[i][0], L[i][1] = L[i][1], L[i][0]

        # Tworze tablice sonsiedztwa
        tablica_sonsiedztwa = [[] for _ in range(vertx_amount)]
        for i in L:
            tablica_sonsiedztwa[i[0]].append(i[1])

        return tablica_sonsiedztwa

    L_soms_rev = rev_edges(L_2, vertex_amnt)

    def harness_ss(timeings, L_soms, vertex_amnt):

        def czy_wszystkie_silne_zebrane(been_here):
            for i in been_here:
                if i == False:
                    return False
            return True

        def index_max_val_z_tablicy(timeings):
            max_index = 0
            for i in range(len(timeings)):
                if (timeings[max_index] == None) or (timeings[i] != None and timeings[i] > timeings[max_index]):
                    max_index = i

            return max_index

        def DFS_silnie_skl(skladowa, orgin, flaga):

            been_here[orgin] = True
            timeings[orgin] = None
            skladowa.append(orgin)

            for i in L_soms[orgin]:
                if been_here[i] == False:
                    DFS_silnie_skl(skladowa, i, flaga + 1)

            if flaga == 0:
                array_of_str_compound.append(skladowa)

        array_of_str_compound = []

        been_here = [False for _ in range(vertex_amnt)]

        while czy_wszystkie_silne_zebrane(been_here) == False:
            silna_skl = []
            max_index = index_max_val_z_tablicy(timeings)
            print(max_index)
            DFS_silnie_skl(silna_skl, max_index, 0)

        return array_of_str_compound

    return harness_ss(timeings,L_soms_rev,vertex_amnt)

print(lista_silnie_skladowych(L_2))
L = [[0,1],[0,2],[2,1,],[2,3],[3,4],[3,5],[4,5]]

def mosciki(L):
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

    def DFS(curr_time,curr_vertex):
        arr_czasy_odwiedzenia[curr_vertex] = curr_time
        # Zaznaczam lov
        lov[curr_vertex] = curr_time
        been_here[curr_vertex] = True

        print(f'curr_ver: {curr_vertex}, lov: {lov}, child: {child}, been_here: {been_here}')
        # Warun końcowy
        def czy_byl_wszendzie(been_here):
            for i in been_here:
                if i == False:
                    return False
            return True

        if czy_byl_wszendzie(been_here) == True:

            # Tera chyba trza znaleźć min krawędź wsteczną
            min_low = lov[curr_vertex]
            for somsiad in L_somsiedztwa[curr_vertex]:
                if lov[somsiad] < min_low:
                    min_low = lov[somsiad]
            lov[curr_vertex] = min_low



        # Przechodzę do następncyh wierchułków
        for next_vertx in L_somsiedztwa[curr_vertex]:
            if been_here[next_vertx] == False:

                # print(f'curr_ver: {curr_vertex}, lov: {lov}, child: {child}, been_here: {been_here}')
                # lov[curr_vertex] = curr_time
                child[curr_vertex] = next_vertx

                DFS(curr_time+1,next_vertx)

            # Tutaj zaktualizuje lov-a ( patrząc na dostępne )
            else:
                print(f'naprawa z patrzenia. lov: {lov}')

                if lov[curr_vertex] != None:
                    if lov[curr_vertex] > lov[next_vertx]:
                        lov[curr_vertex] = lov[next_vertx]
                        print(f'naprawa z patrzenia_2. lov: {lov}')
                        print('')


        # Wracając zmieniam lov-y ( dzięki childrenom )
        print(f'zmieniam lov z childrenami: cur_v: {curr_vertex}, lov: {lov}')
        if child[curr_vertex] != None and lov[curr_vertex] > lov[child[curr_vertex]]:
            lov[curr_vertex] = lov[child[curr_vertex]]

        # Trzeba sprawdzić czy to most
        print(f"spr mostu. arr_czasy: {arr_czasy_odwiedzenia}, lov: {lov}")
        if child[curr_vertex] != None and arr_czasy_odwiedzenia[child[curr_vertex]] == lov[child[curr_vertex]]:
            lista_moscikow.append([curr_vertex,child[curr_vertex]])

    # Teraz trzeba zrobić seeda DFSa

    DFS(1,0)

    return lista_moscikow

print(mosciki(L))
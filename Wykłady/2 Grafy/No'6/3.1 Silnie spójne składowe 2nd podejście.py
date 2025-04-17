L = [[0,1],[2,0],[1,2],[3,4],[5,6],[4,5],[6,3],[9,7],[7,8],[7,10],[10,9],[8,9],[0,10],[2,3],[4,7],[5,9]]
import time
def wyznaczanie_silnie_spójnych_skladowych(L):
    L_copy = L.copy()
    # Jest dużo kodu więc zrobie to całe w odobnej funkcji
    def tmieings_for_vertexes(L):
        # Teraz mi jest potrzebna funkja spr czy zostały jejszcze jakieś krawędzie w graphie
        def is_any_left(L):  # True jeżeli zostały jejszcze jakieś krawędzie
            i = 0
            for i in range(len(L)):
                if L[i] != None and been_here[L[i][1]] == 0:
                    return True
            return False

        # Pomocniczy war do końca rekurzji
        def req_end(origin, L, been_here):
            for i in L:
                # print(f'req end {i}')
                if i != None and i[0] == origin and been_here[i[1]] == 0:
                    return False
            return True

        # Wpierw policzymi ile jest wierzchołków i zrobię tablice z zapisanymi czasami
        vertexes_amount = 0
        for i in L:
            if i[0] > vertexes_amount:
                vertexes_amount = i[0]
            if i[1] > vertexes_amount:
                vertexes_amount = i[1]
        vertexes_amount += 1
        timeings = [[] for _ in range(vertexes_amount)]
        global czas_przetworzenia
        czas_przetworzenia = 1
        n = len(L)
        been_here = [0 for _ in range(vertexes_amount)]

        def DFS(origin, L, been_here):
            # print(f"origin: {origin}, been herer {been_here}, timeings {timeings}")
            # time.sleep(1)
            global czas_przetworzenia

            # Warunek końcowy (Meszqele boss)
            if req_end(origin, L, been_here) == True:
                timeings[origin] = czas_przetworzenia
                czas_przetworzenia += 1
                been_here[origin] = 1
                return

            # Możliwe weirzchołki
            for i in range(n):
                # print(f'i = {i}')
                # Przyszło mi do głowy że trzeba tutaj krawędź wyzerować, krawędź po której nie idziemy ale którą nie można przejść
                if L[i] != None and L[i][0] == origin and been_here[L[i][1]] == 1:
                    L[i] = None

                if L[i] != None and L[i][0] == origin and been_here[L[i][1]] == 0:
                    # print(f'')

                    next_org = L[i][1]
                    L[i] = None
                    been_here[origin] = 1
                    # print(f'next_org {next_org}, org= {origin}')
                    DFS(next_org, L, been_here)

            # No i trzeba jeszcze dodać aktualny wierzchołek
            # print(f'aktualny wierzchołek origin {origin}, czas {czas_przetworzenia}, timeings {timeings}')
            timeings[origin] = czas_przetworzenia
            czas_przetworzenia += 1

            # I hurka durka jeszcze trzeba go hurka durka usunąć
            been_here[origin] = 1

            return

        # Pierwszy DFS-sik
        while is_any_left(L) == True:
            # Tutaj szukam jakiegoś początkowego wierzchołka który jeszcze istnieje
            for i in range(n):
                # print(f'dla zera L[i] = {L[i]}')
                if L[i] != None and been_here[L[i][1]] == 0:
                    break
            origin = L[i][0]

            # Teraz trzeba zacząć robić zwykłego DFS po kolei z zapisaniem czasów
            DFS(origin, L, been_here)

        return timeings

    timeings = tmieings_for_vertexes(L_copy)
    n = len(L)
    print(timeings)
    # Wydaje mi się że będzie op żeby zrobić tablice 2D gdzie mamy nr wierzchołków i czasy

    # Ogolnie teraz trzeba trzeba odwróćić krawyndzie
    L_rev_edges = [[L[i][1],L[i][0]] for i in range(n)]

    # Teraz potrzebuje listy na listy vertexow z ss
    arrray_of_str_comp_cmpts = []

    # Teraz trzeba napisać DFS żeby przechodził po grafie i zapisywał na bierząco numerki

    L_copy_2 = L.copy()
    def harnessing_sil_skl(L_harness,timeings_har):

        def are_all_harnesed(L): # True wszystko zebrane, False-nie
            for i in L:
                if i != None:
                    return False
            return True

        def znajdz_indeks_max(tablica):
            max_index = 0
            for i in range(1, len(tablica)):
                if (tablica[max_index] == None) or (tablica[i] > tablica[max_index]):
                    max_index = i
            return max_index

        def DFS(L,origin,been_here,skladowa):
            print(f"L,origin:{origin},been_here:{been_here},skladowa:{skladowa}, lista_skl: {arrray_of_str_comp_cmpts}")
            # time.sleep(1)
            skladowa.append(origin)
            for i in range(len(L)):
                # print(f'i: {i}, L[i]:{L[i]}, been here: {been_here}')
                if L[i] != None and L[i][0] == origin and been_here[L[i][1]] == 0:
                    org_next = L[i][1]
                    been_here[org_next] = 1
                    L[i] = None
                    timeings_har[origin] = None
                    DFS(L,org_next,been_here,skladowa)

            if skladowa != None:
                arrray_of_str_comp_cmpts.append(skladowa)
                skladowa = None
            return skladowa

        # Trzeba jeszcze been_here tablice zrobić
        vertexes_amount = 0
        for i in L_harness:
            if i[0] > vertexes_amount:
                vertexes_amount = i[0]
            if i[1] > vertexes_amount:
                vertexes_amount = i[1]
        vertexes_amount += 1
        been_here =  [0 for _ in range(vertexes_amount)]
        while are_all_harnesed(timeings_har) == False:
            skladowa = []
            # print(timeings_har)
            # Teraz trzeba wędrować od najwyższych czasów przetworzenia
            max_index = znajdz_indeks_max(timeings_har)
            # print(f'max_i: {max_index}')
            print(arrray_of_str_comp_cmpts)
            DFS(L_harness,max_index,been_here,skladowa)

        return

    harnessing_sil_skl(L_rev_edges,timeings)

    return arrray_of_str_comp_cmpts







print(wyznaczanie_silnie_spójnych_skladowych(L))
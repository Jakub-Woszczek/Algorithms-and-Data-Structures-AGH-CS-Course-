L = [[0,1],[2,0],[1,2],[3,4],[5,6],[4,5],[6,3],[9,7],[7,8],[7,10],[10,9],[8,9],[0,10],[2,3],[4,7],[5,9]]
import time
def wyznaczanie_silnie_spójnych_składowych(L):

    # Teraz mi jest potrzebna funkja spr czy zostały jejszcze jakieś krawędzie w graphie
    def is_any_left(L): # True jeżeli zostały jejszcze jakieś krawędzie
        for i in L:
            if i != None:
                return True
        return False

    # Zrobie casual warunek końcowy do rekurzji (Czy z danego wierzchołak już sie dalej nie pójdzie
    def req_end(origin,L):
        for i in L:
            if i != None and i[0] == origin:
                return False
        return True

    # Zrobie jeszcze kopie tablicy
    L_copy = L.copy()

    # Wpierw policzymi ile jest wierzchołków i zrobię tablice z zapisanymi czasami
    vertexes_amount = 0
    for i in L:
        if i[0] > vertexes_amount:
            vertexes_amount = i[0]
        if i[1] > vertexes_amount:
            vertexes_amount = i[1]
    vertexes_amount +=1
    timeings = [[] for _ in range(vertexes_amount)]
    list_of_str_conn_comp = []
    # nonlocal  czas_przetworzenia
    global czas_przetworzenia
    czas_przetworzenia = 1

    been_here= [0 for _ in range(vertexes_amount)]

    def DFS(origin, L):

        global czas_przetworzenia
        nonlocal been_here
        # print(f"czas prz {czas_przetworzenia}, orging: {origin}, odwiedzone: {been_here}, timeings: {timeings}")

        time.sleep(1)
        # Tu trzeba warunek końcowy
        if req_end(origin, L) == True:
            timeings[origin] = czas_przetworzenia
            czas_przetworzenia += 1
            return

        # Tutaj trzeba przejść do możliwych wierzchołków które nie są nonami
        i = 0
        for i in range(len(L)):
            print(f"origin {origin}, L[i] {L[i]}, been_here[origin] {been_here[origin]}")
            if L[i] != None and L[i][0] == origin and been_here[origin] == 0:
                next_org = L[i][1]
                L[i] = None
                been_here[origin] = 1
                DFS(next_org,L)

        # No i tutaj jeszcze trzeba dodać aktualny wierzchołek
        timeings[origin] = czas_przetworzenia
        czas_przetworzenia += 1

        return


    # Czyli trzeba pierwszego DFSika zrobić
    while is_any_left(L) == True:

        # Tutaj szukam jakiegoś początkowego wierzchołka który jeszcze istnieje
        for i in L:
            if i != None:
                break
        origin = i[0]

        # Teraz trzeba zacząć robić zwykłego DFS po kolei z zapisaniem czasów



        DFS(origin,L)


    return timeings

print(wyznaczanie_silnie_spójnych_składowych(L))
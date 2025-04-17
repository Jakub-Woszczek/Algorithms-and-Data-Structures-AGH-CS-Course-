from egzP3btesty import runtests 
from queue import PriorityQueue

def lufthansa ( G ):
    def z_listy_somsiedztwa_na_krawendziowa(G):
        G_kraw = []

        for row in range(len(G)):
            for col in range(len(G[row])):
                if G[row][col] != None:
                    # Zaznaczyłem wierzchołki dla ułatwienia
                    v1 = row
                    v2 = G[row][col][0]

                    G_kraw.append([v1, v2, G[row][col][1]])
                    G[row][col] = None
                    # Teraz to właściwie musze znaleźć ten drugi wierchułek hurka durka
                    for i in range(len(G[v2])):
                        if G[v2][i] != None:
                            if G[v2][i][0] == v1:
                                G[v2][i] = None
                                break

        return G_kraw, len(G)

    def partition(array, low, high):

        pivot = array[high][2]

        i = low - 1

        for j in range(low, high):
            if array[j][2] >= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        return i + 1

    def quickSort(array, low, high):
        if low < high:
            pi = partition(array, low, high)

            quickSort(array, low, pi - 1)

            quickSort(array, pi + 1, high)

    G_kraw, vertex_amnt = z_listy_somsiedztwa_na_krawendziowa(G)

    # Teraz trzeba by było posortować te krawędzie względem wag
    quickSort(G_kraw, 0, len(G_kraw) - 1)

    # Teraz trzeba zrobić dajmy np color do oznaczania grup i tablice przynanleżności
    color = 1
    w_jakiej_grupie = [None for _ in range(vertex_amnt)]
    max_edge_left = 0
    suma_przelotów = 0

    for i in range(len(G_kraw)):

        v1, v2 = G_kraw[i][0], G_kraw[i][1]

        # Chyba będę Nonować krawędzie których nie biore ale musze jeszcze maxa z pozostałych znaleźż

        # Teraz przypadek jak tworze nowy kolor
        if w_jakiej_grupie[v1] == None and w_jakiej_grupie[v2] == None:
            w_jakiej_grupie[v1], w_jakiej_grupie[v2] = color, color
            color += 1

            # Teraz nie usuwam krawędzi

        # Teraz przypadek jak normalnie dodaje wierzchołek do grupy coloru
        elif (w_jakiej_grupie[v1] != None and w_jakiej_grupie[v2] == None):

            w_jakiej_grupie[v2] = w_jakiej_grupie[v1]

        elif (w_jakiej_grupie[v2] != None and w_jakiej_grupie[v1] == None):

            w_jakiej_grupie[v1] = w_jakiej_grupie[v2]


        # Teraz jak jakiś wierzchołek już jest w tej grupie (trzeba usunąc krawędz )
        elif w_jakiej_grupie[v1] == w_jakiej_grupie[v2]:

            suma_przelotów += G_kraw[i][2]
            max_edge_left = max(max_edge_left, G_kraw[i][2])
            G_kraw[i] = None

        # Teraz jak wierzchołek jest w innej grupie
        if w_jakiej_grupie[v1] != None and \
                w_jakiej_grupie[v2] != None and \
                w_jakiej_grupie[v1] != w_jakiej_grupie[v2]:

            supreme_col = w_jakiej_grupie[v1]
            to_del_col = w_jakiej_grupie[v2]

            # Teraz trzeba zamienić kolorki w drugiej grupie
            for i in range(len(w_jakiej_grupie)):
                if w_jakiej_grupie[i] == to_del_col:
                    w_jakiej_grupie[i] = supreme_col

        i += 1

    return suma_przelotów - max_edge_left
    return 0 

runtests ( lufthansa, all_tests=True )
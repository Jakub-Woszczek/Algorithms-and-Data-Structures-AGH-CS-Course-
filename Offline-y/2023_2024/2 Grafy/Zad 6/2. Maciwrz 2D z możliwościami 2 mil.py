L = [[0, 1, 3, 0],[1, 0, 1, 2],[3, 1, 0, 4],[0, 2, 4, 0]]

def na_2D_macierz(G):
    n = len(G)
    # Trza drugi poziom zrobić
    for i in range(n):
        for j in range(n):
            G[i][j] = [G[i][j],0]

    # Dla każdego wierzchołka sprawdzam somsiadów
    for org in range(n):
        dystans_na_piechote = 0
        for vertex_1 in range(n):  # vertex = 2

            # Sprawdzam czy dany somsiad istnieje
            if G[org][vertex_1][0] != 0:
                dystans_na_piechote += G[org][vertex_1][0]

                # Teraz ide do somsiadów mego somsiada
                for vertex_2 in range(n):

                    # Sprawdzam czy somsiad somsiada istnieje i nie jest orgiem
                    if G[vertex_1][vertex_2][0] != 0 and vertex_2 != org:
                        dystans_na_piechote += G[vertex_1][vertex_2][0]

                        # No i teraz trzeba nadpisać 2 milowe buty
                        print('nadpisuje')
                        G[vertex_1][vertex_2][1] = min(dystans_na_piechote,max(G[org][vertex_1][0],G[vertex_1][vertex_2][0]))


    return G

def print_macierz(macierz):
    # Sprawdzenie, czy argument jest macierzą 3D
    if not isinstance(macierz, list) or not all(isinstance(submatrix, list) for submatrix in macierz):
        print("Błąd: Argument powinien być macierzą 3D, reprezentowaną jako lista list list.")
        return

    # Drukowanie osobno macierzy z pierwszą i drugą wartością
    print("Macierz z pierwszą wartością:")
    for submatrix in macierz:
        for row in submatrix:
            print([row[0]], end=" ")
        print()  # Nowa linia po wydrukowaniu wiersza

    print("Macierz z drugą wartością:")
    for submatrix in macierz:
        for row in submatrix:
            print([row[1]], end=" ")
        print()  # Nowa linia po wydrukowaniu wiersza


print_macierz(na_2D_macierz(L))
def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def highway(A):
    import math

    def are_all_connected(T):
        for el in T:
            if el == False:
                return False
        return True
    def odleglosc(a,b):
        wynik = math.sqrt((a[0] - b[0])**(2) + (a[1] - b[1])**(2))
        return math.ceil(wynik)

    n = len(A)
    T_odleglosci = [[0 for _ in range(n)] for  _ in range(n)]
    T_edges = []


    for row in range(n):
        for col in range(row+1,n):
            if row != col:
                dist = odleglosc(A[row],A[col])
                T_odleglosci[row][col] = dist
                T_odleglosci[col][row] = dist
                T_edges.append([row,col,dist])

    print(T_edges)
    Edges_sorted = sorted(T_edges, key= lambda x : x[2])
    print(Edges_sorted)
    for i in range(len(T_edges)):
        Edges_sorted[i].append(i)
    is_vertes_ocuppied = [False for _ in range(n)]
    vertex_edges_connected = [[] for _ in range(n)]
    is_edge_occupied = [False for _ in range(len(T_edges))]

    # Nwm jakis Cruscall
    curren_min = float('inf')
    curren_max = 0
    for v1,v2,edge,ids in T_edges:
        if are_all_connected(is_vertes_ocuppied) == True: # Tutaj przerywam jeżeli już połączyłem wszystkie miasta
            break

        if is_vertes_ocuppied[v1] == False and is_vertes_ocuppied[v2] == False: # Nowa dwa miasta połączam

            vertex_edges_connected[v1].append(ids)
            vertex_edges_connected[v2].append(ids)
            is_vertes_ocuppied[v1] = True
            is_vertes_ocuppied[v2] = True
            is_edge_occupied[ids] = True
            curren_min = min(curren_min,edge)
            curren_max = max(curren_max,edge)

        elif is_vertes_ocuppied[v1] == False and is_vertes_ocuppied[v2] == True: # Dodaje miasto do sieci

            vertex_edges_connected[v1].append(ids)
            vertex_edges_connected[v2].append(ids)
            is_vertes_ocuppied[v1] = True
            is_edge_occupied[ids] = True
            curren_min = min(curren_min, edge)
            curren_max = max(curren_max, edge)

        elif is_vertes_ocuppied[v1] == True and is_vertes_ocuppied[v2] == False: # Dodaje miasto do sieci

            vertex_edges_connected[v1].append(ids)
            vertex_edges_connected[v2].append(ids)
            is_vertes_ocuppied[v2] = True
            is_edge_occupied[ids] = True
            curren_min = min(curren_min, edge)
            curren_max = max(curren_max, edge)

        elif is_vertes_ocuppied[v1] == True and is_vertes_ocuppied[v2] == True: # Dodaje drogę do sieci

            vertex_edges_connected[v1].append(ids)
            vertex_edges_connected[v2].append(ids)
            is_edge_occupied[ids] = True
            curren_min = min(curren_min, edge)
            curren_max = max(curren_max, edge)

    print(vertex_edges_connected)
    print_straight(T_odleglosci)
    print('')
    print(Edges_sorted)

    print(curren_min,curren_max)

A =[(10,10),(15,25),(20,20),(30,40)]
highway(A)
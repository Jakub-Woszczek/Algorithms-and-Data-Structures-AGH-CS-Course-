def print_straight(T):
    """Funkcja pomocnicza do formatowania i wypisywania tablicy."""
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in
                     range(len(formatted_T[0]))]

    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)


def odleglosc(a, b):
    """Oblicza odległość między dwoma punktami a i b, zaokrągloną w górę."""
    import math
    wynik = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return math.ceil(wynik)


def are_all_connected(T):
    """Sprawdza, czy wszystkie elementy w tablicy są połączone."""
    for el in T:
        if el == False:
            return False
    return True


def prepare_distance_matrix(A):
    """Przygotowuje macierz odległości i listę krawędzi na podstawie współrzędnych miast."""
    n = len(A)
    T_odleglosci = [[0 for _ in range(n)] for _ in range(n)]
    T_edges = []

    for row in range(n):
        for col in range(row + 1, n):
            dist = odleglosc(A[row], A[col])
            T_odleglosci[row][col] = dist
            T_odleglosci[col][row] = dist
            T_edges.append([row, col, dist])

    return T_odleglosci, T_edges


def initialize_variables(n, num_edges):
    """Inicjalizuje zmienne potrzebne do algorytmu."""
    is_vertes_ocuppied = [False for _ in range(n)]
    vertex_edges_connected = [[] for _ in range(n)]
    is_edge_occupied = [False for _ in range(num_edges)]
    return is_vertes_ocuppied, vertex_edges_connected, is_edge_occupied


def update_min_max(curren_min, curren_max, edge):
    """Aktualizuje minimalną i maksymalną wartość krawędzi."""
    curren_min = min(curren_min, edge)
    curren_max = max(curren_max, edge)
    return curren_min, curren_max


def process_edge(v1, v2, edge, ids, is_vertes_ocuppied, vertex_edges_connected, is_edge_occupied, curren_min,
                 curren_max):
    """Przetwarza krawędź i aktualizuje odpowiednie struktury."""
    if is_vertes_ocuppied[v1] == False and is_vertes_ocuppied[v2] == False:
        vertex_edges_connected[v1].append(ids)
        vertex_edges_connected[v2].append(ids)
        is_vertes_ocuppied[v1] = True
        is_vertes_ocuppied[v2] = True
        is_edge_occupied[ids] = True
        curren_min, curren_max = update_min_max(curren_min, curren_max, edge)

    elif is_vertes_ocuppied[v1] == False and is_vertes_ocuppied[v2] == True:
        vertex_edges_connected[v1].append(ids)
        vertex_edges_connected[v2].append(ids)
        is_vertes_ocuppied[v1] = True
        is_edge_occupied[ids] = True
        curren_min, curren_max = update_min_max(curren_min, curren_max, edge)

    elif is_vertes_ocuppied[v1] == True and is_vertes_ocuppied[v2] == False:
        vertex_edges_connected[v1].append(ids)
        vertex_edges_connected[v2].append(ids)
        is_vertes_ocuppied[v2] = True
        is_edge_occupied[ids] = True
        curren_min, curren_max = update_min_max(curren_min, curren_max, edge)

    elif is_vertes_ocuppied[v1] == True and is_vertes_ocuppied[v2] == True:
        vertex_edges_connected[v1].append(ids)
        vertex_edges_connected[v2].append(ids)
        is_edge_occupied[ids] = True
        curren_min, curren_max = update_min_max(curren_min, curren_max, edge)

    return curren_min, curren_max


def kruskal_algorithm(T_edges, is_vertes_ocuppied, vertex_edges_connected, is_edge_occupied, n):
    """Główna logika algorytmu Kruskala do łączenia miast."""
    curren_min = float('inf')
    curren_max = 0

    for v1, v2, edge, ids in T_edges:
        if are_all_connected(is_vertes_ocuppied):
            break
        curren_min, curren_max = process_edge(v1, v2, edge, ids, is_vertes_ocuppied, vertex_edges_connected,
                                              is_edge_occupied, curren_min, curren_max)

    return curren_min, curren_max


def highway(A):
    """Funkcja główna rozwiązująca problem minimalizacji czasu budowy autostrad."""
    n = len(A)

    # Przygotowanie danych: macierz odległości i lista krawędzi
    T_odleglosci, T_edges = prepare_distance_matrix(A)

    # Sortowanie krawędzi według odległości
    Edges_sorted = sorted(T_edges, key=lambda x: x[2])

    # Dodanie indeksów do krawędzi
    for i in range(len(Edges_sorted)):
        Edges_sorted[i].append(i)

    # Inicjalizacja zmiennych
    is_vertes_ocuppied, vertex_edges_connected, is_edge_occupied = initialize_variables(n, len(Edges_sorted))

    # Wykonanie algorytmu Kruskala
    curren_min, curren_max = kruskal_algorithm(Edges_sorted, is_vertes_ocuppied, vertex_edges_connected,
                                               is_edge_occupied, n)



    # Wypisanie wyników
    print(f'Edges_sorted {Edges_sorted}')
    print(f'is_vertes_ocuppied {is_vertes_ocuppied}')
    print(f'vertex_edges_connected {vertex_edges_connected}')
    print(f'is_edge_occupied {is_edge_occupied}')

# Testowy przypadek
A = [(10, 10), (15, 25), (20, 20), (30, 40)]
highway(A)

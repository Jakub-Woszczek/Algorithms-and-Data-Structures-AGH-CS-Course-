from queue import PriorityQueue


def islands(G, A, B):
    n = len(G)

    # Koszt za transport: 1 - most, 5 - prom, 8 - lot
    TRANSPORT_COST = {1: 1, 5: 5, 8: 8}

    # Każdy węzeł ma 3 możliwe stany: dotarliśmy tam mostem (1), promem (5), lub samolotem (8)
    # Stąd potrzebujemy 3x większej tablicy kosztów
    dist = [[float('inf')] * 3 for _ in range(n)]

    pq = PriorityQueue()

    # Dodajemy startową wyspę A, zaczynając od każdego rodzaju transportu
    for t, cost in TRANSPORT_COST.items():
        pq.put((0, A, t))
        dist[A][t // 3] = 0

    while not pq.empty():
        current_cost, island, transport = pq.get()

        # Jeżeli dotarliśmy do wyspy B, zwracamy minimalny koszt
        if island == B:
            return current_cost

        # Iterujemy po sąsiadach
        for neighbor in range(n):
            connection = G[island][neighbor]
            if connection != 0 and connection != transport:
                next_transport = connection
                next_cost = current_cost + TRANSPORT_COST[next_transport]
                idx = next_transport // 3

                if dist[neighbor][idx] > next_cost:
                    dist[neighbor][idx] = next_cost
                    pq.put((next_cost, neighbor, next_transport))

    return None


import random


def generate_random_graph(size, density=0.3):
    """
    Generuje losowy graf o podanym rozmiarze i gęstości.

    Parametry:
    - size: liczba węzłów (wysp).
    - density: gęstość grafu, czyli procent wypełnienia macierzy sąsiedztwa.

    Zwraca:
    - macierz sąsiedztwa reprezentującą graf.
    """
    G = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(i + 1, size):
            if random.random() < density:
                connection_type = random.choice([1, 5, 8])  # Losowo wybierz typ połączenia
                G[i][j] = connection_type
                G[j][i] = connection_type  # Graf jest nieskierowany

    return G


def run_tests(test_count=10, graph_size=7, density=0.3):
    """
    Uruchamia testy porównujące wyniki funkcji islands na losowo generowanych grafach.

    Parametry:
    - test_count: liczba testów do przeprowadzenia.
    - graph_size: rozmiar grafu (liczba węzłów).
    - density: gęstość grafu.
    """
    for i in range(test_count):
        G = generate_random_graph(graph_size, density)

        # Wybierz losowe wyspy A i B
        A = random.randint(0, graph_size - 1)
        B = random.randint(0, graph_size - 1)

        # Uruchom funkcję islands
        result = islands(G, A, B)

        # Wyświetl wyniki testów
        print(f"Test {i + 1}:")
        print(f"Graf: {G}")
        print(f"Start: {A}, Koniec: {B}, Wynik: {result}")
        print()

run_tests()
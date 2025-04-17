# FAILEDDDDDDDDDDDDDDDD
# Trzeba pisać osobną dikstrie do tego że jest łapówka na każdym odc, bo
# wtedy drogi się róznią (można zrobić tak że dodaje na początku do każdego
# edge doddaje r i wtedy pójdzie







from queue import PriorityQueue


def gold(G, V, s, t, r):
    n = len(G)

    # Funkcja Dijkstry, która oblicza minimalne odległości oraz liczbę krawędzi od wierzchołka 'start'
    def dijkstra(G, start):
        distances = [float('inf')] * n
        edge_count = [0] * n
        distances[start] = 0
        Q = PriorityQueue()
        Q.put((0, start))

        while not Q.empty():
            curr_weight, curr_vertex = Q.get()

            if curr_weight > distances[curr_vertex]:
                continue

            for neighbor, edge_weight in G[curr_vertex]:
                new_dist = curr_weight + edge_weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    edge_count[neighbor] = edge_count[curr_vertex] + 1
                    Q.put((new_dist, neighbor))
                elif new_dist == distances[neighbor]:
                    # Jeśli mamy dwie ścieżki o tym samym dystansie, wybieramy tę z mniejszą liczbą krawędzi
                    edge_count[neighbor] = min(edge_count[neighbor], edge_count[curr_vertex] + 1)

        return distances, edge_count

    # Najkrótsze ścieżki od `s` do wszystkich wierzchołków
    dist_from_start, _ = dijkstra(G, s)

    # Najkrótsze ścieżki od `t` do wszystkich wierzchołków
    dist_from_end, edge_count_to_t = dijkstra(G, t)

    # Minimalny koszt bez napadu na zamek
    min_cost = dist_from_start[t]

    # Przechodzimy przez każdy wierzchołek (zamek) i obliczamy koszt z napadem
    for v in range(n):
        if dist_from_start[v] < float('inf') and dist_from_end[v] < float('inf'):
            # Koszt przejścia z s do v oraz z v do t z uwzględnieniem napadu
            cost_with_raid = dist_from_start[v] + (dist_from_end[v] * 2 + edge_count_to_t[v] * r) - V[v]

            # Dodane printy do debugowania
            print(f"Wierzchołek: {v}")
            print(f"  Odległość z {s} do {v}: {dist_from_start[v]}")
            print(f"  Odległość z {v} do {t}: {dist_from_end[v]}")
            print(f"  Liczba krawędzi z {v} do {t}: {edge_count_to_t[v]}")
            print(
                f"  Koszt z napadem (dist_from_start[v] + 2 * dist_from_end[v] + edge_count_to_t[v] * r - V[v]): {cost_with_raid}")
            print(f"  Obecny minimalny koszt: {min_cost}")

            min_cost = min(min_cost, cost_with_raid)
            print(f"  Zaktualizowany minimalny koszt: {min_cost}\n")

    return min_cost


G = [[(1,9), (2,2)], # 0
[(0,9), (3,2), (4,6)], # 1
[(0,2), (3,7), (5,1)], # 2
[(1,2), (2,7), (4,2), (5,3)], # 3
[(1,6), (3,2), (6,1)], # 4
[(2,1), (3,3), (6,8)], # 5
[(4,1), (5,8)] ] # 6
V = [25,30,20,15,5,10,0]
s = 0
t = 6
r = 7
print(gold(G,V,s,t,r))
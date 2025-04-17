# DIkstria find shortest path +
import heapq
def jumper( G, s, w ):
       def dijkstra_with_paths(graph, start, end):
              n = len(graph)
              distances = [float('inf')] * n  # Tablica odległości
              distances[start] = 0

              paths = [[] for _ in range(n)]  # Tablica ścieżek
              paths[start] = [[start]]  # Ścieżka startowa

              pq = [(0, start)]  # Kolejka priorytetowa (dystans, wierzchołek)

              while pq:
                     current_dist, current_vertex = heapq.heappop(pq)

                     if current_dist > distances[current_vertex]:
                            continue

                     for neighbor, weight in enumerate(graph[current_vertex]):
                            if weight > 0:  # Sprawdzamy tylko istniejące krawędzie
                                   distance = current_dist + weight

                                   if distance < distances[neighbor]:
                                          distances[neighbor] = distance
                                          paths[neighbor] = [path + [neighbor] for path in paths[current_vertex]]
                                          heapq.heappush(pq, (distance, neighbor))
                                   elif distance == distances[neighbor]:
                                          paths[neighbor].extend([path + [neighbor] for path in paths[current_vertex]])

              return paths[end-1]

       def macierz_na_liste_sasiedztwa(G):
              T = []
              for i in range(len(G)):
                     sasiad = []
                     for j in range(len(G[i])):
                            if G[i][j] != 0:
                                   sasiad.append([j, G[i][j]])
                     T.append(sasiad)
              return T

       G_sons = macierz_na_liste_sasiedztwa(G)
       n = len(G_sons)

       been_here = [False for _ in range(n)]


       paths = dijkstra_with_paths(G,s,w)

       def dq_path_check(T,G_sons):
              n = len(T)
              DQ_moge = [float('inf') for _ in range(n)]
              DQ_nie_moge = [float('inf') for _ in range(n)]

              for i in range(0,n-1):
                     curr_v,next_v = T[i],T[i+1]

                     for somsiad, edge in G_sons[curr_v]:
                            if somsiad == next_v:
                                   DQ_moge[next_v] = min(DQ_moge[next_v],min(DQ_moge[curr_v],DQ_nie_moge[curr_v]) + edge)

                                   if i < n - 3:
                                          for somsiad_2, edge_2 in G_sons[next_v]:
                                                if somsiad_2 == T[i+2]:
                                                       DQ_nie_moge[somsiad_2] = DQ_moge[curr_v] + max(edge,edge_2)

              return min(DQ_moge[n-1],DQ_nie_moge[n-1])

       min_p = float('inf')
       for T in paths:
              min_p= min(min_p,dq_path_check(T,G_sons))

       print(min_p)










T_1 = [[0, 1], [1, 0]]
T_2 = [[0, 2, 0], [2, 0, 3], [0, 3, 0]]
T_3 = [[0, 1, 0, 0], [1, 0, 2, 0], [0, 2, 0, 3], [0, 0, 3, 0]]
T_4 = [[0, 1, 3, 0], [1, 0, 1, 2], [3, 1, 0, 4], [0, 2, 4, 0]]
T_5 = [[0, 1, 3, 4, 0],
       [1, 0, 0, 2, 0],
       [3, 0, 0, 5, 6],
       [4, 2, 5, 0, 3],
       [0, 0, 6, 3, 0]]

T_6 = [[0, 1, 0, 0, 0, 0],
       [1, 0, 2, 2, 0, 0],
       [0, 2, 0, 0, 3, 0],
       [0, 2, 0, 0, 3, 0],
       [0, 0, 3, 3, 0, 1],
       [0, 0, 0, 0, 1, 0]]

T_7 = [[0, 1, 200, 200, 200, 200],
       [1, 0, 2, 200, 200, 200],
       [200, 2, 0, 40, 200, 200],
       [200, 200, 40, 0, 40, 200],
       [200, 200, 200, 40, 0, 117],
       [200, 200, 200, 200, 117, 0]]

T_8 = [[0, 9, 5, 0, 0],
       [9, 0, 0, 1, 0],
       [5, 0, 0, 9, 0],
       [0, 1, 9, 0, 10],
       [0, 0, 0, 10, 0]]

jumper(T_5,0,5)
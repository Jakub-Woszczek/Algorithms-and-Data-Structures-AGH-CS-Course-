# Jakub Woszczek

# Mój algorytm opiera się na puszczeniu dwa razy diksty do Każdego wierzchołka w grafie
# z wierzchołka s i t. Wtedy forem ide po każdym wierzchołku i rozważam czy biore
# tam rower. mając juz min dystans z s do tego wierzchołka i z tego wierzchołka do t
# to łatwo juz policzyć całkowitą droge i zaokrąglić

# Złożoność to dwa razy dikstria i jeden for po każdym wierzchołku czyli O( ElogV )

from egz1atesty import runtests


def armstrong( B, G, s, t):
  from queue import PriorityQueue

  def z_l_kraw_na_L_sons(G):
    all_v = 0
    for v1, v2, w in G:
      all_v = max(all_v, v1, v2)
    all_v += 1

    L_sons = [[] for _ in range(all_v)]

    for v1, v2, w in G:
      L_sons[v1].append([v2, w])
      L_sons[v2].append([v1, w])
    return L_sons, all_v

  L_sons, all_v = z_l_kraw_na_L_sons(G)  # L_sons w postaci [ index , waga_kr ]

  # Dikstria do wszystkich krawędzi

  def dikstria_no_bike(G_sons, all_v, start):

    Q = PriorityQueue()
    been_here = [False for _ in range(all_v)]
    distances = [float('inf') for _ in range(all_v)]

    # Dodaje pierwszy wierzchołek
    Q.put([0, start])
    distances[start] = 0

    while not Q.empty():

      curr_dist, curr_v = Q.get()
      been_here[curr_v] = True

      for soms, edge in G_sons[curr_v]:
        distances[soms] = min(distances[soms], curr_dist + edge)

        if been_here[soms] == False:
          next_dist = curr_dist + edge
          Q.put([next_dist, soms])

    return distances

  no_bike_dist_all = dikstria_no_bike(L_sons, all_v, s)

  def dikstria_with_bike(G_sons, all_v, start):

    Q = PriorityQueue()
    been_here = [False for _ in range(all_v)]
    distances = [float('inf') for _ in range(all_v)]

    # Dodaje pierwszy wierzchołek
    Q.put([0, start])
    distances[start] = 0

    while not Q.empty():

      curr_dist, curr_v = Q.get()
      been_here[curr_v] = True

      for soms, edge in G_sons[curr_v]:
        distances[soms] = min(distances[soms], curr_dist + edge)

        if been_here[soms] == False:
          next_dist = curr_dist + edge
          Q.put([next_dist, soms])

    return distances

  do_mety_z_rowerem = dikstria_with_bike(L_sons, all_v, t)

  def extract_smallest_bike_rating(B, all_V):

    rating = [None for _ in range(all_V)]

    for vertex, licznik, mianownik in B:

      if rating[vertex] == None:
        rating[vertex] = [licznik, mianownik]

      else:
        prev_l, prev_mian = rating[vertex]
        if prev_l / prev_mian > licznik / mianownik:
          rating[vertex] = [licznik, mianownik]
    return rating

  extract_ratings = extract_smallest_bike_rating(B, all_v)

  min_with_bike = float('inf')
  multiply = [float('inf'), 1]
  for vertex, l, m in B:
    min_with_bike = min(min_with_bike, (no_bike_dist_all[vertex] + l * do_mety_z_rowerem[vertex] / m) // 1)

  return min(min_with_bike, no_bike_dist_all[t])
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )

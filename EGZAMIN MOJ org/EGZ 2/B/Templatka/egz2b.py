# Jabkub Woszczek

# Algorytm ten to implementacja algorytmu dikstry, gdzie mam dodatkowe kroki
# dodające zmiane torów.

# Złożoność tego algorytmu to O(mlog(m))

from egz2btesty import runtests


def tory_amos( E, A, B ):
  from queue import PriorityQueue
  max_v = 0
  for x, y, dist, typ in E:
    max_v = max(max_v, x, y)

  G_sons = [[] for _ in range(max_v + 1)]
  Distances = [float('inf') for _ in range(max_v + 1)]
  been_here = [False for _ in range(max_v + 1)]

  for x, y, dist, typ in E:
    G_sons[x].append([y, dist, typ])
    G_sons[y].append([x, dist, typ])


  Q = PriorityQueue()  # Przyjmuje krotki typu (dystans przejechany, curr_v,typ poprzedni transportu,obciążenie do zmiany torów)

  Q.put((A, 0))
  curr_v, dist = Q.get()
  Distances[curr_v] = dist
  been_here[curr_v] = True

  for neighbour, neigh_dist, typ in G_sons[curr_v]:
    Q.put((neigh_dist, neighbour, typ, 0))

  while not Q.empty():

    distance, curr_v, typ, change_time = Q.get()
    been_here[curr_v] = True

    Distances[curr_v] = min(Distances[curr_v], distance + change_time)  # Na początku daje dystans
    if curr_v == B:
      return Distances[curr_v]

    for neighbour, neigh_dist, next_typ in G_sons[curr_v]:

      if been_here[neighbour] == False:

        if typ == next_typ: # Sprawdzam tyt
          if typ == 'I':
            next_change = 5

          else:
            next_change = 10

        else:
          next_change = 20

        Q.put((Distances[curr_v] + neigh_dist, neighbour, next_typ, next_change)) # Dodaje do kolejki wraz ze zmianą torów

  return Distances[B]
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )

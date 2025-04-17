# Jakub Woszczek

# Mój algorytm do zmodifikowany alg. Dikstry  który na bierząco sprawdza
# czy przekroczył 16h i to dodaje do odległości.

# Złożoność tego algorytmu to O( ElogV )

from kol2testy import runtests

def warrior( G, s, t):


  def sonsiedztwo_vertexes(L):

    # Licze wierzchołki
    vertx_amount = 0
    for i in L:
      if i[0] > vertx_amount:
        vertx_amount = i[0]
      if i[1] > vertx_amount:
        vertx_amount = i[1]
    vertx_amount += 1

    # Tworze tablice sonsiedztwa
    tablica_sonsiedztwa = [[] for _ in range(vertx_amount)]
    for i in L:
      tablica_sonsiedztwa[i[0]].append([i[1], i[2]])
      tablica_sonsiedztwa[i[1]].append([i[0], i[2]])

    return tablica_sonsiedztwa, vertx_amount

  def Dikstria_z_przystankami(G_kraw, start, meta):

    from queue import PriorityQueue

    # Tworzę listę sąsiedztwa
    G_sons, v_amnt = sonsiedztwo_vertexes(G_kraw)

    # Teraz trzeba stworzyć priority queue,
    Q = PriorityQueue()
    timeings = [float('inf') for _ in range(v_amnt)]
    been_here = [False for _ in range(v_amnt)]

    # Trzeba dodać pierwszy wierzchołek, !!!!!!!! Kolejka w postaci: [timeing,vertex,curr_exhaust]
    timeings[start] = 0
    Q.put([timeings[start], start, 0])


    while not Q.empty():

      v = Q.get()
      curr_distance, curr_vertex, curr_tiredness = v[0], v[1], v[2]


      # Tutaj sprawdzam czy doszedł do celu
      if curr_vertex == meta:
        return timeings[curr_vertex]

      for i in range(len(G_sons[curr_vertex])):

        next_vertex, edge_weight = G_sons[curr_vertex][i][0], G_sons[curr_vertex][i][1]

        if been_here[next_vertex] == False:

          # Teraz trza by zrobić relaxamcje i ją podziele na 2

          # Teraz jak dojdę do następnego bez przerwy
          if curr_tiredness + edge_weight <= 16:

            if timeings[next_vertex] > timeings[curr_vertex] + edge_weight:
              timeings[next_vertex] = timeings[curr_vertex] + edge_weight

              Q.put([timeings[next_vertex], next_vertex, curr_tiredness + edge_weight])

          else:

            # Tutaj dodam przystanek

            # I robie to samo
            if timeings[next_vertex] > timeings[curr_vertex] + edge_weight + 8:
              timeings[next_vertex] = timeings[curr_vertex] + edge_weight + 8

              Q.put([timeings[next_vertex], next_vertex, 0])

  return Dikstria_z_przystankami(G, s, t)
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = False )

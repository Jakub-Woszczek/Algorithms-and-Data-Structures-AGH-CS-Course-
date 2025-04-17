# Jakub Woszczek
#
# Działanie mojego kodu polega na przeszukiwaniu DFS danego grafu
# z zapisywaniem max_wysokości i min_wysokości by ta nie była większa
# niż 2*t. Bardziej szczegółowy opis jest na bieżąco z kodem.
#
# Złożoność szacuje na O(V+E)
#
#
from zad4testy import runtests

def Flight(L,x,y,t):

  # Szukam ile jest wszystkich wieszchołków
  num_of_vertices = 0
  for i in range(len(L)):
    if L[i][0] > num_of_vertices:
      num_of_vertices = L[i][0] + 1
    elif L[i][1] > num_of_vertices:
      num_of_vertices = L[i][1] + 1
  num_of_vertices += 1

  # Teraz stowrzę tablice tablic która będzie reprezentować
  # każdy wieszchołek (index to wieszchołek), i bedzie w formie
  # T_v = [(2,2000), ....] gdzie index to nr wieszchołka a
  # T_v[0][0] to index wieszchołka z którym jest połączony

  T_if_visited = [None] * num_of_vertices
  T_ver = [[] for _ in range(num_of_vertices)]
  for index in range(num_of_vertices):
    for i in range(len(L)):
      if L[i][0] == index:
        T_ver[index].append([L[i][1], L[i][2]])
      if L[i][1] == index:
        T_ver[index].append([L[i][0], L[i][2]])

  # Tutaj zaimplementowałem funkcje DFS (Dla kolejnych  wierzchołków
  def DFS(v_start, T_ver, min_attitude, max_attitiude, destination):
    # Sprawdzam czy juz dotarłem do celu
    if v_start == destination:
      return True

    # Zaznaczam że obecny jest odwiedzony
    T_if_visited[v_start] = 1

    # Idę dalej do możliwych sąsiadów
    for somsiad in T_ver[v_start]:
      index_somsiada = somsiad[0]
      height = somsiad[1]
      #Tutaj sprawdzam czy już nie byłem tam
      if T_if_visited[index_somsiada] != 1:

        # Tutaj sprawdzę czy wysokości się zgadzają
        if height >= min_attitude and height <= max_attitiude: # Jeżeli height jest pomiędzy min i max
          if DFS(index_somsiada, T_ver, min_attitude, max_attitiude, destination) == True:
            return True

        if height < min_attitude and max_attitiude - height <= 2 * t: # Jeżeli height jest niżej niż min, min->height
          if DFS(index_somsiada, T_ver, height, max_attitiude, destination) == True:
            return True

        if height > max_attitiude and height - min_attitude <= 2 * t: # Jeżeli height jest wyżej niż max, max->height
          if DFS(index_somsiada, T_ver, min_attitude, height, destination) == True:
            return True

    T_if_visited[v_start] = None # Backtracking do rekurencji

  # Tutaj zaczynam pierwszy wieszchołek
  T_if_visited[x] = 1
  for i in T_ver[x]:
    # Ustalam pierwsze min i max
    min_at = i[1]
    max_at = i[1]
    neighboor = i[0]
    if DFS(neighboor, T_ver, min_at, max_at, y) == True:
      return True

  return False
  return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )

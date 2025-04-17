from kolutesty import runtests

def projects(n, L):
  def lista_somsiedztwa(n, L):

    List_soms = [[] for i in range(n)]

    for next, first in L:
      List_soms[first].append(next)

    return List_soms

  L_soms = lista_somsiedztwa(n, L)

  been_here = [False for _ in range(n)]
  dfs_timeings = [1 for _ in range(n)]

  def DFS(vertex):
    been_here[vertex] = True
    if len(L_soms[vertex]) == 0:
      dfs_timeings[vertex] = 1

    else:
      max_time = 0
      for somsiad in L_soms[vertex]:
        if been_here[somsiad] == False:
          max_time = max(max_time, DFS(somsiad))
        else:
          max_time = max(max_time, dfs_timeings[somsiad])
      dfs_timeings[vertex] = max_time + 1

    return dfs_timeings[vertex]

  max_len = 0
  for v_org in range(n):

    if been_here[v_org] == False:
      max_len = max(max_len, DFS(v_org))

  return max_len
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )

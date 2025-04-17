# Jakub Woszczek

# Mój algorytm to implementacja algorytmu BFS z każdego źródła, i
# zwiększanie go o jedną krawędź z każdą iteracją. Mam specjalną
# kolejkę 'Q_fight' gdzie zapisuje wierzchołki do sprawdzenia
# który index w nich wygrał i zapisanie tego w tablicy.

# Szacuje złożoność tego na O(V + E) gdyż jest to w
# sumie BFS jeden tylko że podzielony.

from egz3atesty import runtests


def mykoryza( G,T,d ):
  from queue import Queue


  ilosc_grzybow = len(T)
  n = len(G)  # Ilość drzew
  czy_wszystkie_drzewa_podbite = n # Będe od tego dodejmował 1 z każdym podbitym drzewem, żeby wiedzieć kiedy skończyć
  lagrest_realm = [1 for _ in range(ilosc_grzybow)]  # Dam na 1 wiedząc że dany grzyb ma na początku już jedno drzewo
  current_przynaleznosc = [None for _ in range(n)]  # To jest tablica gdzie zapisuje jaki grzyb ma dane drzewo
  fight = [[] for _ in range(n)]  # Tutaj dodaje indexy grzybów które w danej jednostce czasu walczą o to drzewo
  treest_conquered = [False for _ in range(n)]  # Tutaj zapisuje już zdobyte drzewa
  fight_check = [False for _ in
                 range(n)]  # To jest tablica pomocnicza żeby wiedzieć czy w danej jednosce sprawdziłem dane drzewo

  Q = Queue()  # Wsadzamy do niej krotki typu [wierzcholek,rodzaj grzyba]
  Q_fight = Queue()  # Tutaj dodaje wierzchołki które w danej jednosce są podbinaje

  # Przygotuje kolejke, zaznaczam źródła
  for i in range(ilosc_grzybow):
    Q.put([T[i], i])
    treest_conquered[T[i]] = True  # Zaznaczam że dane drzewo jest już zajęte przez grzyba
    current_przynaleznosc[T[i]] = i  # Zaznaczam że dane drzewo ma tego grzyba
    czy_wszystkie_drzewa_podbite -= 1

  while czy_wszystkie_drzewa_podbite > 0:  # Warunek kończoncy wszystkie BFS-y

    while not Q.empty():  # Robie BFS z każdego źródła grzyba
      curr_v, index_grzyba = Q.get()

      for somsiad in G[curr_v]:
        if treest_conquered[somsiad] == False:  # Sprawdzam czy nie jest już zajęty przez innego grzyba
          fight[somsiad].append(index_grzyba)
          Q_fight.put(somsiad)  # Dodaje wierzchołek do sprawdzenia

    # Teraz mam sytuacje gdzie w 'fight' mam indexy walczących grzybów w danym drzewie więc trzeba wyciągnąć zwycięzce
    while not Q_fight.empty():
      vertchx_to_check = Q_fight.get()
      if fight_check[vertchx_to_check] == False:
        i = vertchx_to_check
        winner = min(fight[i])
        current_przynaleznosc[i] = winner  # Tutaj wyciągam zwycięzce walki
        treest_conquered[i] = True  # I daje że drzewo jest zdobyte
        Q.put([i, winner])  # Dodaje jeszcze do następnej jednostki czasu wierzchołek i zwycięsce
        lagrest_realm[winner] += 1 # Dodaje kolejne drzewo dla danego grzyba

        fight[i] = []  # I oczywiście trzba oczyścić pole walki
        fight_check[vertchx_to_check] = True # I zapisać żeby nie sprawdzać znowy tego wierzchołka
        czy_wszystkie_drzewa_podbite -= 1

    fight_check = [False for _ in range(n)]


  return lagrest_realm[d] # Zwracam odpowiedni grzyb
  return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )

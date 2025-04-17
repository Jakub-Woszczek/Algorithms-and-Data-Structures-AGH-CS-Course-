def mykoryza(G,T,d):
    from queue import Queue
    def are_all_trees_conquered(T):
        for el in T:
            if el == False:
                return False

        return True

    # Plan działania:
    # 1. wsadzić do kolejki zwykłej / tablicy ( żeby wiedzieć ile jest w danym przedziale czasu
    # 2. BFs z każdego

    # G - tablica sąsiedztwa
    # T - tablica T[i] - nr wierzchołka gdzie się gdzyb zaczyna
    # d -index wybranego grzyba

    ilosc_grzybow = len(T)
    n = len(G) # Ilość drzew
    lagrest_realm = [1 for _ in range(ilosc_grzybow)] # Dam na 1 wiedząc że dany grzyb ma na początku już jedno drzewo
    current_przynaleznosc = [None for _ in range(n)]
    fight = [[] for _ in range(n)] # Tutaj dodaje indexy grzybów które w danej iteracji walczą o to drzewo :3
    treest_conquered = [False for _ in range(n)]

    Q = Queue() # Wsadzamy do niej krotki typu [wierzcholek,rodzaj grzyba]
    Q_fight = Queue() # Tutaj dodaje wierzchołki gdzie będzie trzeba zdecydować

    # Przygotuje kolejke
    for i in range(ilosc_grzybow):
        Q.put([T[i],i])
        treest_conquered[T[i]] = True # Zaznaczam że dane drzewo jest już zajęte przez grzyba
        current_przynaleznosc[T[i]] = i # Zaznaczam że dane drzewo ma tego grzyba


    while are_all_trees_conquered(treest_conquered) == False:

        while not Q.empty(): # Robie BFS z każdego źródła grzyba
            curr_v, index_grzyba = Q.get()


            for somsiad in G[curr_v]:
                if treest_conquered[somsiad] == False: # Sprawdzam czy nie jest już zajęty przez innego grzyba
                    fight[somsiad].append(index_grzyba)
                    Q_fight.put(somsiad) # Dodaje wierzchołek do sprawdzenia

        # Teraz mam syt gdzie w 'fight' mam walczące grzyby w danym drzewie więc trzeba wyciągnąć zwycięzce
        for i in range(n):
            if len(fight[i]) > 0 :
                winner = min(fight[i])
                current_przynaleznosc[i] = winner  # Tutaj wyciągam zwycięzce walki
                treest_conquered[i] = True # I daje że drzewo jest zdobyte
                Q.put([i,winner]) # Dodaje jeszcze do następnej jednostki czasu wierzchołek i zwycięsce
                print(f'daje do kolejki vertex {i} z indexem grzyba {winner}')
                lagrest_realm[winner] += 1

                print(f'zwycięzcą w wierzchołku: {i} jest {winner}')
                fight[i] = [] # I oczywiście trzba oczyścić pole walki

        print(lagrest_realm)

    return lagrest_realm[d]

G = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[7,5]]
T = 8,2,6
d = 1

mykoryza(G,T,d)



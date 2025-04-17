def dominance(P):
    # i_domi = 0
    # x_domi,y_domi = P[0]
    n = len(P)
    i = 1
    list_of_dominated = []

    while n > 0:
        i_domi = 0
        x_domi, y_domi = P[0]
        while i < n:  # Szukam podciągu z jednym dominatorem
            if P[i][0] < x_domi and P[i][1] < y_domi:  # Szukam pierwszej max pkt
                list_of_dominated.append(P[i])
                del P[i]
                n -= 1  # Chyba skracam tablice

            elif P[i][0] > x_domi and P[i][1] > y_domi:  # Znalazłem nowego dominatora
                list_of_dominated.append(P[i_domi])
                x_domi, y_domi = P[i]
                del P[i_domi]
                i_domi = i
                n -= 1
            i += 1
        poprawka = 0
        while poprawka < n:  # Sprawdzam dla resztek
            if P[poprawka][0] < x_domi and P[poprawka][1] < y_domi:  # Szukam pierwszej max pkt
                list_of_dominated.append(P[poprawka])
                del P[poprawka]
                n -= 1  # Chyba skracam tablice

            poprawka += 1

    return list_of_dominated

P=[[1,1],[2,2],[3,2],[2,4],[4,1],[3,3],[5,5],[5,3],[3,5],[7,6],[6,5]]
print(dominance(P))


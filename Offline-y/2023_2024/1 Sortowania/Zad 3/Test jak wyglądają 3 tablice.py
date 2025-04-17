import random

def generuj_punkty(ile_punktow):
    punkty = []
    for _ in range(ile_punktow):
        x = random.randint(1, 100)  # Generowanie losowej wartości x z przedziału od 1 do 100
        y = random.randint(1, 100)  # Generowanie losowej wartości y z przedziału od 1 do 100
        punkty.append((x, y))
    return punkty

# Przykładowe użycie:
ile_punktow = 15  # Określ, ile punktów chcesz wygenerować
# wygenerowane_punkty = generuj_punkty(ile_punktow)
# print(wygenerowane_punkty)

def dominance(P):
    n = len(P)
    list_of_dominated_1 = []
    list_of_dominated_2 = []
    list_of_dominated_3 = []

    i = 1
    i_domi = 0
    x_domi, y_domi = P[0]
    # tworze list dom 1
    while i < n:
        if P[i][0] <= x_domi and P[i][1] <= y_domi:  # Szukam pierwszej max pkt
            list_of_dominated_1.append(P[i])
            del P[i]
            n -= 1  # Chyba skracam tablice

        elif P[i][0] > x_domi and P[i][1] > y_domi:  # Znalazłem nowego dominatora
            list_of_dominated_1.append(P[i_domi])
            x_domi, y_domi = P[i]
            del P[i_domi]
            i_domi = i
            n -= 1
        i += 1

    poprawka = 0

    while poprawka < n:
        if poprawka != i_domi:
            if P[poprawka][0] <= x_domi and P[poprawka][1] <= y_domi:  # Szukam pierwszej max pkt
                list_of_dominated_1.append(P[poprawka])
                del P[poprawka]
                n -= 1  # Chyba skracam tablice
        poprawka +=1

    # tworze list dom 2
    while i < n:
        if P[i][0] <= x_domi and P[i][1] <= y_domi:  # Szukam pierwszej max pkt
            list_of_dominated_2.append(P[i])
            del P[i]
            n -= 1  # Chyba skracam tablice

        elif P[i][0] > x_domi and P[i][1] > y_domi:  # Znalazłem nowego dominatora
            list_of_dominated_2.append(P[i_domi])
            x_domi, y_domi = P[i]
            del P[i_domi]
            i_domi = i
            n -= 1
        i += 1

    poprawka = 0

    while poprawka < n:
        if poprawka != i_domi:
            if P[poprawka][0] <= x_domi and P[poprawka][1] <= y_domi:  # Szukam pierwszej max pkt
                list_of_dominated_2.append(P[poprawka])
                del P[poprawka]
                n -= 1  # Chyba skracam tablice
        poprawka +=1


    d_1 = len(list_of_dominated_1)
    d_2 = len(list_of_dominated_2)
    n = len(P)

    cnt_max = 0

    # Dla max z dom_1
    x_domi, y_domi = list_of_dominated_1[d_1-1]
    cnt = d_1-1
    for i in range(d_2):
        if list_of_dominated_2[i][0] <= x_domi and list_of_dominated_2[i][1] <= y_domi:
            cnt +=1
    for i in range(n):
        if P[i][0] <= x_domi and P[i][1] <= y_domi:
            cnt +=1

    if cnt > cnt_max:
        cnt_max = cnt

    x_domi, y_domi = list_of_dominated_2[d_2 - 1]
    cnt = d_2 - 1
    for i in range(d_1):
        if list_of_dominated_1[i][0] <= x_domi and list_of_dominated_1[i][1] <= y_domi:
            cnt +=1
    for i in range(n):
        if P[i][0] <= x_domi and P[i][1] <= y_domi:
            cnt +=1

    if cnt > cnt_max:
        cnt_max = cnt

    return list_of_dominated_1,list_of_dominated_2,P
test = [(37, 43), (34, 98), (85, 90), (57, 99), (44, 59), (87, 96), (65, 62), (47, 83), (76, 62), (54, 12), (27, 9), (65, 79), (34, 98), (6, 93), (50, 53)]
x,y,z = dominance(test)
print(x)
print(y)
print(z)
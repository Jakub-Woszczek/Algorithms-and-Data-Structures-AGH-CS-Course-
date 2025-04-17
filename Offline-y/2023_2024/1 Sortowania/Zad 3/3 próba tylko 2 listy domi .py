def dominance(P):
    n = len(P)

    if n > 20:
        list_of_dominated_1 = []
        list_of_dominated_2 = []

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
            poprawka += 1

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
            poprawka += 1

        d_1 = len(list_of_dominated_1)
        d_2 = len(list_of_dominated_2)
        n = len(P)

        cnt_max = 0

        # Dla max z dom_1
        x_domi, y_domi = list_of_dominated_1[d_1 - 1]
        cnt = d_1 - 1
        for i in range(d_2):
            if list_of_dominated_2[i][0] <= x_domi and list_of_dominated_2[i][1] <= y_domi:
                cnt += 1
        for i in range(n):
            if P[i][0] <= x_domi and P[i][1] <= y_domi:
                cnt += 1

        if cnt > cnt_max:
            cnt_max = cnt

        x_domi, y_domi = list_of_dominated_2[d_2 - 1]
        cnt = d_2 - 1
        for i in range(d_1):
            if list_of_dominated_1[i][0] <= x_domi and list_of_dominated_1[i][1] <= y_domi:
                cnt += 1
        for i in range(n):
            if P[i][0] <= x_domi and P[i][1] <= y_domi:
                cnt += 1

        if cnt > cnt_max:
            cnt_max = cnt

        return cnt_max

    else:
        cnt_max = 0
        for i in range(len(P)):
            cnt = 0
            x, y = P[i]

            for i in range(0, i):
                if P[i][0] > x and P[i][1] > y:
                    break
                if P[i][0] < x and P[i][1] < y:
                    cnt += 1
            for i in range(i + 1, len(P)):
                if P[i][0] > x and P[i][1] > y:
                    break
                if P[i][0] < x and P[i][1] < y:
                    cnt += 1

            if cnt > cnt_max:
                cnt_max = cnt

        return cnt_max






P = [(1, 3), (3, 4), (4, 2), (2, 2)]
print(dominance(P))
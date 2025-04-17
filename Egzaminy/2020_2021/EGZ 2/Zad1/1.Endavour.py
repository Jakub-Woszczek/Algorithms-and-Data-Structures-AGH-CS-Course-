def intuse(I,x,y):
    from queue import Queue


    I_cleaned = []
    possible_active_ints = [[False] for _ in range(y+1)]
    trurly_active_ints = [False for _ in range(y+1)]

    index = 0
    for a,b in I:
        if a >= x and b <= y:
            I_cleaned.append([a-x,b-x,index])

            possible_active_ints[a - x][0] = True
            possible_active_ints[b-x][0] = True

            possible_active_ints[a - x].append([a-x,b-x,index])
        index += 1



    I_cleaned.sort(key=lambda x : x[0])
    trurly_active_przedzialy = [False for _ in range(len(I))]
    x, y = 0, y - x

    Q = Queue()
    i = 0
    print(I_cleaned)
    while I_cleaned[i][0] == 0: # Ta funkcja dodaje możliwe początki do kolejki ( Odcinki co się zaczynają na 0)

        Q.put((I_cleaned[i][1],I_cleaned[i][2]))
        i += 1

    possible = []
    while not Q.empty():
        possible.clear()
        prawy,index_form_Q = Q.get()

        def spr_path(prawy,lista_aktywnych_indexuw):
            if prawy >= y: # Warun końcowy
                if prawy == y:
                    for i in lista_aktywnych_indexuw:
                        print(f'dodaje przedział {i} z listy indexow {lista_aktywnych_indexuw}')
                        trurly_active_przedzialy[i] = True
                        trurly_active_ints[I[i][0]] = True
                        trurly_active_ints[I[i][1]] = True
                    return
                else:
                    return None
                # Dodaj do trurly active ints

            if possible_active_ints[prawy][0] == True:

                if trurly_active_ints[prawy] == True:
                    for i in lista_aktywnych_indexuw:
                        print(f'dodaje przedział {i} z listy indexow {lista_aktywnych_indexuw}')
                        trurly_active_przedzialy[i] = True
                        trurly_active_ints[I[i][0]] = True
                        trurly_active_ints[I[i][1]] = True
                    return

                for i in range(1,len(possible_active_ints[prawy])):
                    new_a, new_b, new_index = possible_active_ints[prawy][i]

                    lista_aktywnych_indexuw.append(index)
                    spr_path(new_b, lista_aktywnych_indexuw)
                    lista_aktywnych_indexuw.pop()

        spr_path(prawy,possible.append(index_form_Q))


    print(trurly_active_przedzialy)

I = [[3,4],[2,5],[1,3],[4,6],[1,4]]
x = 1
y = 6
intuse(I,x,y)

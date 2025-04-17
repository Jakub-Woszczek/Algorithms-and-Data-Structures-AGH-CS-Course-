def lamps_print(T):
    T_to = []
    for i in T:
        if i == 0:
            T_to.append('Z')
        elif i == 1:
            T_to.append("C")
        else:
            T_to.append('N')

    for i in T_to:
        print(i,end=' ')
    print('')


def lamps(n,L):

    swiatelka = [0 for _ in range(n+1)]
    blue_max = 0
    curr_blue = 0

    for a,b in L:

        for i in range(a,b+1):
            if swiatelka[i] == 0:
                swiatelka[i] +=1

            elif swiatelka[i] == 1:
                swiatelka[i] += 1
                curr_blue += 1

            elif swiatelka[i] == 2:
                swiatelka[i] = 0
                curr_blue -= 1

        blue_max = max(blue_max,curr_blue)




    return blue_max

n = 9
L = [(0, 4), (2, 6), (1, 6), (2, 5), (7, 9), (1, 7), (1, 7), (1, 7)]
print(lamps(n,L))
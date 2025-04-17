def lamps(n,L):

    swiatelka = [0 for _ in range(n+1)]
    blue_max = 0

    for a,b in L:

        for i in range(a,b+1):
            if swiatelka[i] != 2: swiatelka[i] +=1
            else: swiatelka[i] = 0

        niebieskie = 0
        for swiatelko in swiatelka:
            if swiatelko == 2:
                niebieskie += 1

        blue_max = max(blue_max,niebieskie)

    return blue_max


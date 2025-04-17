def planets( D, C, T, E ):

    Odleglosc_w_latach_swietlych = D # Odległosć i-tej od pierwszej
    Cena_paliwa = C # Na danej planecie
    Teleporty = T # Index - z jakiej planty  i krotka indexu [na jaką,koszt]
    limit_paliwa = E
    ilosc_planet = len(D)

    for i in range(ilosc_planet): # Tutaj pousuwam niepotrzebne teleporty
        if T[i][0] == i:
            Teleporty[i] = None

    DQ = [[float('inf') for _ in range(ilosc_planet)] for _ in range(limit_paliwa + 1)]

    for i in range(limit_paliwa+1): # Robie seeda da dynamiqa
        DQ[i][0] = i*Cena_paliwa[0]

    if Teleporty[0] != None:
        destination,price = Teleporty[0]

        for i in range(limit_paliwa+1):# Robie seeda da dynamiqa (teleport z 0 planety jeżeli istnieje)
            DQ[i][destination] = price + i*Cena_paliwa[destination]

    for curr_planeta in range(1,ilosc_planet):
        next_dist = Odleglosc_w_latach_swietlych[curr_planeta] - Odleglosc_w_latach_swietlych[curr_planeta-1]

        DQ[0][curr_planeta] = min(DQ[0][curr_planeta],DQ[next_dist][curr_planeta-1])
        for i in range(1,E-next_dist+1):
            DQ[i][curr_planeta] = min(DQ[i-1][curr_planeta]+Cena_paliwa[curr_planeta],
                                      DQ[i+next_dist][curr_planeta-1])

        while i < E:
            i += 1
            DQ[i][curr_planeta] = DQ[i - 1][curr_planeta] + Cena_paliwa[curr_planeta]

        if T[curr_planeta] != None:
            teleport_na,cena = T[curr_planeta][0],T[curr_planeta][1]

            DQ[0][teleport_na] = min(DQ[0][teleport_na],
                                     DQ[0][curr_planeta] + cena)

        # for bruh in DQ:
        #     print(bruh)
        # print('')
    return DQ[0][ilosc_planet-1]

D = [ 0, 5, 10, 20]
C = [ 2, 1, 3, 9]
T = [(2,3), (3,7), (2,10), (3,10)]
E = 10
print(planets(D,C,T,E))

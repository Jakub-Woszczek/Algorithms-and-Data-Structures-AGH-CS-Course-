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


    for planeta in range(1,ilosc_planet):
        for ilosc_paliwa in range(E+1):

            DQ[ilosc_paliwa][planeta] = min(DQ[ilosc_paliwa][planeta],
                                            float('inf') if ilosc_paliwa + (D[planeta] - D[planeta-1]) > E else DQ[ilosc_paliwa + D[planeta] - D[planeta-1]][planeta-1],
                                            DQ[ilosc_paliwa-1][planeta] + C[planeta])

        # Tutaj zakutalizuje teleport
        if Teleporty[planeta] != None:
            destination, price = Teleporty[planeta]
            start_price = DQ[0][planeta]

            for i in range(E+1):
                DQ[i][destination] = min(DQ[i][destination],start_price + price + i*Cena_paliwa[destination])


    for bruh in DQ:
        print(bruh)

    return DQ[0][ilosc_planet-1]


D = [ 0, 5, 10, 20]
C = [ 2, 1, 3, 9]
T = [(2,3), (3,7), (2,10), (3,10)]
E = 10

planets(D,C,T,E)


def snow( S ):

    S.sort()
    S.reverse()
    suma = 0

    for i in range(len(S)):
        suma =suma + S[i] - i if S[i] - i > 0 else suma

    return suma


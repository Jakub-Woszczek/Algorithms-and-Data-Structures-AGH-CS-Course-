from egz1atesty import runtests

def snow( S ):
    S.sort()
    S.reverse()
    suma = 0

    for i in range(len(S)):
        suma = suma + S[i] - i if S[i] - i > 0 else suma

    return suma
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )

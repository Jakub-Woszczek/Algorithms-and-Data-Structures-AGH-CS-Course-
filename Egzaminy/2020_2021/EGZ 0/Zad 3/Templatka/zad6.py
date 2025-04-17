from zad6testy import runtests

def jumper( G, s, w ):

    print(G)
    print('')
    for bruh in G:
        print(bruh)
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )
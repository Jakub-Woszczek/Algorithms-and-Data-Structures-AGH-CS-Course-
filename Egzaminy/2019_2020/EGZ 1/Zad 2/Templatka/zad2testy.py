#########################################################



test_tabs = [[-999, -1000, 1001, 1000],  # [-999,-1000] [1000,1001]
             [3, 2, -3, 4, 5, -9],  # [-3,-9] [2,3,4,5]
             [3, 6, 9, -8, -6, -3]] # [-3,-6,-8] [3,6,9]
test_costs = [998, 4, 5]

def runtests( f ):
    OK = True
    for t, c in zip(test_tabs, test_costs):
        cost = f(t)
        print('Tablica: {0:30s}'.format(str(t)), end='')
        if cost == c:
            print('OK.      Największa wartosc bezwzgledna: ', str(cost))
        else:
            OK = False
            print('BLAD!    Największa wartosc bezwzgledna: {0:4d};'.format(cost), '   Powinno byc: ', str(c))
    print("----------------------------")
    if OK:
        print("OK!")
    else:
        print("Bledy!")

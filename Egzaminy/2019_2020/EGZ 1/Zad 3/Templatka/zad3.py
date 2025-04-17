from zad3testy import runtests
import math




                 
    
def fast_sort(tab, a):
    tab.sort()

    T = []
    for wykladnik in tab:
        T.append(a ** (wykladnik))

    return T



runtests( fast_sort )

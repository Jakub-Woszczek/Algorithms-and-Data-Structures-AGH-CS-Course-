# Jeżeli
def fast_sort(tab,a):

    tab.sort()

    T = []
    for wykladnik in tab:
        T.append(a**(wykladnik))

    return T

def opt_sum(T):
    T_negs = []
    T_posit = []

    for el in T:
        if el > 0:
            T_posit.append(el)
        else:
            T_negs.append(el)



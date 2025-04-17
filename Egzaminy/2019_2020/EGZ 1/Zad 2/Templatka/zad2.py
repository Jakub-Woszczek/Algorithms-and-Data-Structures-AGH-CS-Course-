from zad2testy import runtests




def opt_sum(T):
    T = sorted(T)

    n = len(T)
    curr_sum = 0
    max_dif = 0

    prawo = n - 1
    lewo = 0
    if T[prawo] > abs(T[lewo]):
        curr_sum += T[prawo]
        prawo -= 1
    else:
        curr_sum += T[lewo]
        lewo += 1

    while lewo <= prawo:

        if curr_sum > 0:
            curr_sum += T[lewo]
            lewo += 1

        elif curr_sum < 0:
            curr_sum += T[prawo]
            prawo -= 1

        else:
            if abs(T[lewo]) > T[prawo]:
                curr_sum += T[prawo]
                prawo -= 1

            else:
                curr_sum += T[lewo]
                lewo += 1

        max_dif = max(max_dif, abs(curr_sum))

    return max_dif
    return 0



runtests( opt_sum )

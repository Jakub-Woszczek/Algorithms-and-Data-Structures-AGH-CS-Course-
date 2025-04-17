

def wired(T):
    n = len(T)

    # Ustawiam tablice gdzie mam zapisaną różnice mocy między każdymi dwoma wejściami
    T_roznicy_mocy = [[0 for _ in range(n)] for _ in range(n)]

    all_voltage = 0

    for j in range(n):
        for i in range(n):
            if i != j:
                T_roznicy_mocy[j][i] = abs(T[i] - T[j])
                T_roznicy_mocy[i][j] = abs(T[i] - T[j])

    def min_z_T(T):


        nonlocal all_voltage
        lenght = len(T)
        if lenght == 2:
            return T_roznicy_mocy[T[0]][T[1]]

        suma_curr = T[0] + T[len(T) - 1]
        for i in range(1,lenght,2):
            suma_curr += min(min_z_T(T[i:]) + min_z_T(T[i:]))

        return suma_curr


    suma_min = float('inf')

    for i in range(1, n, 2):
        suma_min = min(min_z_T(T[i:]) + min_z_T(T[i:]), suma_min)


    return suma_min


T = [7,1,3,7,2,1]

print(wired(T))




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

    def max_z_T(T):
        nonlocal all_voltage
        suma_min = float('inf')
        lenght = len(T)
        for i in range(1,lenght,2):
            suma_min = min(max_z_przedzialu(0,i) + max_z_T(T[i:]),suma_min)



    def max_z_przedzialu(a,b): # Max jeżeli a i b są połączone
        nonlocal all_voltage
        suma_r_naipecn = 0
        voltage = float('inf')

        if b-a == 1:
            return T_roznicy_mocy[a,b]



        voltage = max(voltage,max_z_T(T[a:b]))

        suma_r_naipecn += voltage

        return suma_r_naipecn







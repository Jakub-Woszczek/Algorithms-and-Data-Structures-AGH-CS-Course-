def wired(T):
    def max_z_a_b(T_r):
        # War graniczny requrzji
        if len(T_r) == 0:
            return 0

        if len(T_r) == 2:
            return abs(T_r[0] - T_r[1])

        n = len(T_r)
        ab_max = float('inf')
        for i in range(3, len(T_r), 2):
            srodek = max_z_a_b(T_r[1:n-1]) + abs(T[0] - T[n-1])
            lewy_przedzial = max_z_a_b(T_r[1:i - 2]) + abs(T_r[0] - T_r[i - 2])
            prawy_przedzial = max_z_a_b(T_r[i:n - 1]) + abs(T_r[i - 1] - T_r[n - 1])
            ab_max = min(ab_max, lewy_przedzial + prawy_przedzial,srodek)

        return ab_max

    n = len(T)
    ab_max = float('inf')
    for i in range(3, len(T), 2):
        print(T[1:i-2])
        print(f'krańce {T[0]}, {T[i-2]}')
        print(T[i:n-1])
        print(f'krańce {T[i-1]}, {T[n - 1]}')
        print('')

        srodek = max_z_a_b(T[1:n-1]) + abs(T[0] - T[n-1])
        lewy_przedzial = max_z_a_b(T[1:i - 2]) + abs(T[0] - T[i - 2])
        prawy_przedzial = max_z_a_b(T[i:n - 1]) + abs(T[i - 1] - T[n - 1])
        ab_max = min(ab_max, lewy_przedzial + prawy_przedzial,srodek)

    print(ab_max)
    return ab_max + n / 2

T = [7,1,3,7,2,1,3,7,6,3,2,3,4,2,6,1]
T2 = [39, 90, 72, 7, 65, 80, 30, 82, 19, 73, 94, 18, 29, 1] # 140 -> 133 bez n/2
print(wired(T2))
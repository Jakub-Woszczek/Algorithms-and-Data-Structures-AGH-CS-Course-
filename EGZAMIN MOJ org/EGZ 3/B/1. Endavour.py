def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def kunlucky(T, k):

    # Wpierw zrobie tablice kolejnych liczb pechowych <= max(T)
    # Później muszę sprawdzić które z liczb z T są pechowe
    # Później EZ dynamiq

    def T_pech_creator(T,k):
        prof_max_num = max(T)

        T_pechowa = [k]
        prev = k
        i = 2
        while prev < prof_max_num:
            num = prev + prev % (i-1) + 7
            T_pechowa.append(num)
            i += 1
            prev = num

        return T_pechowa,prev+1

    n = len(T)
    T_pechowa,max_num = T_pech_creator(T,k)
    T_all = [False for _ in range(max_num+1)]
    for el in T_pechowa:
        T_all[el] = True


    L_ciongi = []
    L_czy_unlucky = []
    strike = 0

    def przygotowanie_do_DQ(T,L_ciongi,L_czy_unlucky,T_check):

        i = 0
        strike = 0
        for num in T:
            if T_all[num] == True:
                if strike > 0:
                    L_ciongi.append(strike)
                    L_czy_unlucky.append(False)
                L_ciongi.append(1)
                L_czy_unlucky.append(True)
                strike = 0

            else:
                strike += 1

        if strike > 0:
            L_ciongi.append(strike)
            L_czy_unlucky.append(False)

        return L_ciongi,L_czy_unlucky


    L_ciongi,L_czy_unlucky = przygotowanie_do_DQ(T,L_ciongi,L_czy_unlucky,T_all)


    DQ = [[None for _ in range(len(L_ciongi))] for _ in range(3)]
    max_possible = 0


    for i in range(len(L_ciongi)):
        if L_czy_unlucky[i] == True:
            DQ[0][i] = 0

        else:
            DQ[0][i] = L_ciongi[i]





    if L_czy_unlucky[0] == True:

        DQ[1][0] = 1

        for col in range(1,len(L_ciongi)):
            for row in range(1,3):

                if L_czy_unlucky[col] == False:
                    if DQ[row][col-1] != None:
                        DQ[row][col] = DQ[row][col-1] + L_ciongi[col]
                        max_possible = max(max_possible, DQ[row][col])


                else:
                    if DQ[row-1][col-1] != None:
                        DQ[row][col] = DQ[row-1][col-1] + L_ciongi[col]
                        max_possible = max(max_possible, DQ[row][col])



    else:
        for col in range(1, len(L_ciongi)):
            for row in range(1, 3):

                if L_czy_unlucky[col] == False:
                    if DQ[row][col - 1] != None:
                        DQ[row][col] = DQ[row][col - 1] + L_ciongi[col]
                        max_possible = max(max_possible, DQ[row][col])


                else:
                    if DQ[row - 1][col - 1] != None:
                        DQ[row][col] = DQ[row - 1][col - 1] + L_ciongi[col]
                        max_possible = max(max_possible, DQ[row][col])




    print(L_ciongi)
    print('')
    print_straight(DQ)


    # for col in range(len(L_ciongi)):
    #
    #     for row in range(3):




    # print(T_pechowa)

    return max_possible

T = [11,10,19,19,17,16,3,9,6,14,13,8,2,13,11,12,5,5,5]
k = 3
kunlucky(T,k)


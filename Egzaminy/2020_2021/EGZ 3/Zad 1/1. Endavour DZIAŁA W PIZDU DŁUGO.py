def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def mr( X ):
    n = len(X)
    # Narazie znajde podciąg ściśle rosnący
    def last_form_list(T):
        return T[len(T) - 1]
    def max_rising_potciong(T):
        def copy_and_append(T, element):

            T_copy = []
            for el in T:
                T_copy.append(el)

            if element != None:
                T_copy.append(element)
            return T_copy




        n = len(T)
        DQ = [[None for _ in range(n)] for _ in range(n)]
        szczyty = [1 for _ in range(n)]

        DQ[1][0] = [X[0]]

        for i in range(1,n):
            DQ[1][i] =  [max(DQ[1][i-1][0],X[i])]


        for col in range(1,n):
            for row in range(2,col+ 2):
                if row == n or DQ[row-1][col-1] == None:
                    break


                if DQ[row][col-1] != None:
                    if last_form_list(DQ[row][col-1]) < X[col] and X[col] < last_form_list(DQ[row-1][col-1]): # Spr między zamianą ostatniego
                        DQ[row][col] = copy_and_append(DQ[row-1][col-1],X[col])
                        szczyty[col] = max(szczyty[col],row)

                    else:
                        DQ[row][col] = copy_and_append(DQ[row][col-1],None)
                        szczyty[col] = max(szczyty[col], row)

                else:
                    if last_form_list(DQ[row-1][col-1]) > X[col]:
                        DQ[row][col] = copy_and_append(DQ[row-1][col-1],X[col])
                        szczyty[col] = max(szczyty[col], row)

        print_straight(DQ)
        print(szczyty)
        return DQ,szczyty

    def merege_two(T_forward, T_to_reverse, meging_point):
        T_end = []
        T_to_reverse = T_to_reverse[::-1]
        if meging_point == last_form_list(T_forward) and meging_point == T_to_reverse[0]:
            for el in T_forward:
                T_end.append(el)

            for i in range(1, len(T_to_reverse)):
                T_end.append(T_to_reverse[i])

        else:
            for el in T_forward:
                T_end.append(el)

            for el in T_to_reverse:
                T_end.append(el)

        return T_end



    DQ_descending,descending_tops = max_rising_potciong(X)
    X.reverse()
    DQ_riseing,rising_tops = max_rising_potciong(X)
    X.reverse()

    najdluzszczy_podciong = []

    for i in range(len(rising_tops)):

        T_rising = DQ_riseing[rising_tops[n-i-1]][n-i-1]
        T_descending = DQ_descending[descending_tops[i]][i]
        merging_point = X[i]

        # print(f'mwrgi {merging_point}, T_rising: {DQ_riseing[rising_tops[i]][i]}, T_descending: {DQ_descending[descending_tops[i]][n-1-i]} ')
        if len(merege_two(T_rising,T_descending,merging_point)) > len(najdluzszczy_podciong) :
            najdluzszczy_podciong = merege_two(T_descending,T_rising,merging_point)


    return najdluzszczy_podciong




X =  [4,10,5,1,5,2,3,4]
X_rev = [4,3,2,5,1,5,10,4]
print(mr(X))

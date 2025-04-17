def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)


L_ciongi = [3,1,5,1,7,1,4,1]
L_czy_unlucky = [False,True,False,True,False,True,False,True]
DQ = [[None for _ in range(len(L_ciongi))] for _ in range(3)]

for i in range(len(L_ciongi)):
    if L_czy_unlucky[i] == True:
        DQ[0][i] = 0

    else:
        DQ[0][i] = L_ciongi[i]

if L_czy_unlucky[0] == True:

    DQ[1][0] = 1

    for col in range(1, len(L_ciongi)):
        for row in range(1, 3):

            if L_czy_unlucky[col] == False:
                if DQ[row][col - 1] != None:
                    DQ[row][col] = DQ[row][col - 1] + L_ciongi[col]


            else:
                if DQ[row - 1][col - 1] != None:
                    DQ[row][col] = DQ[row - 1][col - 1] + L_ciongi[col]

                else:
                    DQ[row][col] = L_ciongi[col]

else:
    for col in range(1, len(L_ciongi)):
        for row in range(1, 3):

            if L_czy_unlucky[col] == False:
                if DQ[row][col - 1] != None:
                    DQ[row][col] = DQ[row][col - 1] + L_ciongi[col]


            else:
                if DQ[row - 1][col - 1] != None:
                    DQ[row][col] = DQ[row - 1][col - 1] + L_ciongi[col]


print(L_ciongi)
print('')

print_straight(DQ)
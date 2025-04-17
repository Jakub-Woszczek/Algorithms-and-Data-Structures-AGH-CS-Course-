def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def zbigniew(A):

    n = len(A)
    all_snacks = 0
    for snack in A:
        all_snacks += snack

    DQ = [[None for _ in range(n)] for _ in range(all_snacks+1)]
    tops = [0 for _ in range(n+1)]

    DQ[0][0] = 0
    for i in range(1,A[0]+1):
        DQ[1][i] = A[0] - i
        tops[i] = 1

    # print_straight(DQ)
    for col in range(1,n):
        top = tops[col]

        for row in range(top + 1):
            if DQ[row][col] != None and A[col] != 0:
                energy = DQ[row][col] + A[col]
                for i in range(1,energy + 1):
                    if i + col < n:
                        if i + col == n-1:
                            return row+1
                        if DQ[row + 1][col + i] != None:
                            DQ[row + 1][col + i] = max(DQ[row + 1][col + i], energy - i)
                            tops[col + i] = row + 1

                        else:
                            DQ[row + 1][col + i] = energy - i
                            tops[col + i] = row + 1



            print_straight(DQ)
            print('')
    search = 0
    while search < all_snacks:
        if DQ[search][n-1] != None:
            return search
        search += 1
    return -1

T = [2,2,1,0,0,0]
A = [2, 2, 1, 0, 0, 0]
A2 = [4,5,2,4,1,2,1,0]
print(zbigniew(A2))
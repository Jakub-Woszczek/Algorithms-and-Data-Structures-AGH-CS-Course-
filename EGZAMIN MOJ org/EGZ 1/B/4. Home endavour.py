def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def kstrong( T, k):
    n = len(T)

    DQ = [[0 for _ in range(n)] for _ in range(k+1)]

    DQ[0][0] = T[0]

    for i in range(1,n):
        DQ[0][i] = max(DQ[0][i-1] + T[i],T[i])

    for  i in range(0,k):
        DQ[i+1][i] = 0

    overall_max = 0

    for row in range(1,k+1):
        for  col in range(row,n):
            DQ[row][col] = max(DQ[row-1][col-1],DQ[row][col-1] + T[col])
            overall_max = max(overall_max,DQ[row][col])

    return overall_max
        print_straight(DQ)
        print('')

    overall_max = 0
    for i in range(k+1):
        overall_max = max(overall_max,DQ[i][n-1])

    return overall_max

T = [-20, 5, -1, 10, 2, -8, 10]
T_1 = [-36, -37, -8, -13, -48, -23, -38, -9, 56, -33, 10, -9, -20, -47, 38, -1, 44, 65, 42, 7, -22, -5, -10, 83, -28, 73, -26, -7, -20, 81, -46, -13, -34, -33, -44, -21, -44, -43, 82, -37, -44, -41, 2, -5, -12, -27, -46, 91, 72, -7, -30, -21, -20, -45, -46, 23, -6, -29, -22, -3, -46, -49, -12, -15, -4, 57, -20, -35, -8, -43, -28, -39, -40, -9, -44, -15, -20, -19, -40, -21, -44, -3, 22, -45, -10, -15, -10, -11, 24, -35, 54, 3, -2, -9, 54, 75, -20, -45, -10, 51, -36, 89, -10, -7, -40, -33, 34, -49, -6, -23, 50, 75, -16, -29, -24, -5, -14, -21, -48, -11, -12, -7, -40, -49, 84, -27, -46, 27, -6, -49, -18, -3, -12, -7, -8, 67, -12, 29, -40, -3, -18, -3, -32, 11, -14, -39, -4, 31, -18, -43, -16, -49, 4, -15, 18, -35, 12, -29, 30, 15, -40, -9, -44, -39, -46, -17, -44, -37, -34, 17, -32, -47, -36, -37, 42, -3, -40, -39, 18, 91, 68, -15, -46, 83, -40, 61, -48, -23, -24, 93, -50, -23, -20, -23, 98, -45, -40, -3, 2, -23]
k = 20
kstrong(T,2)

# Wynik algorytmu  :  661


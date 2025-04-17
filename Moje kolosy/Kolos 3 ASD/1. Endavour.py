def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def orchard(T,m):

    print('asfgkshdbf')
    n = len(T) # Ilość drzew
    all_fruits = 0
    T.sort()
    T.reverse()
    T_sorted = []

    for val in T: # Tutaj mam same niepodzielne i znich mogę zrobić kombinacje dodawania max liczby drzew żeby się zgadzało
        if val % m != 0:
            T_sorted.append(val)






    for i in T:
        all_fruits += i

    if all_fruits%m == 0:
        return 0

    DQ = [[0 for _ in range(n+1)] for _ in range(n)] # Val opisuje ilość owoców, row -> ilość wyciętych, col -> ile drzew rozpatrujemy


    for i in range(1,n+1):
        DQ[0][i] = T_sorted[i-1] + DQ[0][i-1]

    print('kureewaaaaaaaaaa')
    print_straight(DQ)


    for rows in range(1,n):
        for cols in range(rows,n+1):
            if DQ[rows-1][cols] % m == 0:
                DQ[rows][cols]




T = [2,2,7,5,1,14,7]
m = 7
print(orchard(T,m))
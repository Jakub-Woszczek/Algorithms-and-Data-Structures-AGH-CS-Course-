def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in
                     range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)


def orchard(T, m):

    def wybor_sumy(T_1,org_index):
        sum_of_choosen = 0
        choosen_ones = []
        lenght = len(T_1)
        while org_index < lenght and sum_of_choosen<m:
            if sum_of_choosen +  T_1[org_index] <= m:
                print(f'dodaje T_1[org_index] {T_1[org_index]}')
                sum_of_choosen += T_1[org_index]
                choosen_ones.append(org_index)

            org_index += 1

        print(f'spr {sum_of_choosen}')
        if sum_of_choosen%m == 0 and sum_of_choosen != 0:
            print(f'pykło')
            T_left = []
            for i in range(len(T_1)):
                if i not in choosen_ones:
                    T_left.append(T_1[i])

            return T_left
        return T_1


    T.sort()
    T.reverse()
    T_sorted = []

    for val in T:  # Tutaj mam same niepodzielne i znich mogę zrobić kombinacje dodawania max liczby drzew żeby się zgadzało
        if val % m != 0:
            T_sorted.append(val)

    n = len(T_sorted)  # Ilość drzew
    all_fruits = 0
    print(T_sorted)

    for i in T:
        all_fruits += i

    if all_fruits % m == 0:
        return 0

    i = 0
    while i < n:
        T_sorted = wybor_sumy(T_sorted,i)
        i += 1
        print(T_sorted)

    return len(T_sorted)

T = [2,2,7,5,1,14,7]
m = 7
print(orchard(T,m))
def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def orchard(T, m):
    def find_unique_in_sorted(sorted_array, m):
        if not sorted_array:
            return []

        unique_elements = [sorted_array[0]]

        for i in range(1, len(sorted_array)):
            reszta = sorted_array[i] % m
            if reszta != 0:
                unique_elements.append(reszta)

        return unique_elements

    T.sort()
    T = find_unique_in_sorted(T, m)
    all_fruits = sum(T)
    all_trees = len(T)

    DQ = [[None for _ in range(all_trees + 1)] for _ in range(all_fruits + 1)]

    for i in range(1, all_trees + 1):  # Ustawienie ścięcia wszystkich drzew
        DQ[0][i] = i

    DQ[T[0]][1] = 0  # Ustawiam pierwsze drzewo na nie ścięte

    for cols in range(1, all_trees):
        for rows in range(0, all_fruits):

            if DQ[rows][cols] != None:
                DQ[rows][cols + 1] = DQ[rows][cols] + 1 if DQ[rows][cols + 1] == None or DQ[rows][cols + 1] > DQ[rows][
                    cols] else DQ[rows][cols + 1]
                DQ[rows + T[cols]][cols + 1] = DQ[rows][cols] if DQ[rows + T[cols]][cols + 1] == None or \
                                                                 DQ[rows + T[cols]][cols + 1] > DQ[rows][cols] else \
                DQ[rows + T[cols]][cols + 1]

    min_cut_threes = float('inf')
    for i in range(0, all_fruits + 1, m):
        if DQ[i][all_trees] != None:
            min_cut_threes = min(min_cut_threes, DQ[i][all_trees])

    return min_cut_threes

T = [2, 2, 7, 5, 1, 14, 7]
m = 7

print(orchard(T,m))
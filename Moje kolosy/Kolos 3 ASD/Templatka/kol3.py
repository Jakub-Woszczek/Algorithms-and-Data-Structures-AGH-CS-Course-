# Jakub Woszczek

# Problem ten można rozwiązać podobnie do problemu knapsack. ( Można na początku usunąć z rozważań te drzewa które mają od razu podzielna liczbe jabłek)
# Kolumny to nr. drzew a wiersze to ilość jabłek
# DQ[row][col] to MIN ilość wyciętych drzew by być w danym z daną ilośćią jabłek

# Wynik to min z ostatniej kolumny z wierszy podzielnych przez m.

# Złożonosć tego algorytmu to O(n^2)

from kol3testy import runtests


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

    DQ = [[all_trees for _ in range(all_trees + 1)] for _ in range(m)]

    DQ[0][0] = 0

    for cols in range(0, all_trees):
        for rows in range(0, m):

            if DQ[rows][cols] != None:
                DQ[rows][cols + 1] = DQ[rows][cols] + 1 if DQ[rows][cols + 1] > DQ[rows][cols] else DQ[rows][cols + 1]

                DQ[(rows + T[cols]) % m][cols + 1] = DQ[rows][cols] if DQ[(rows + T[cols]) % m][cols + 1] > DQ[rows][
                    cols] else DQ[(rows + T[cols]) % m][cols + 1]

    return DQ[0][all_trees]
    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)

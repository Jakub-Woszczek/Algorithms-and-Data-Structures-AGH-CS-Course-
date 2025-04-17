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

                DQ[(rows + T[cols])%m][cols+1] = DQ[rows][cols] if DQ[(rows + T[cols])%m][cols+1] > DQ[rows][cols] else DQ[(rows + T[cols])%m][cols+1]

    return DQ[0][all_trees]

T = [2, 2, 7, 5, 1, 14, 7]
m = 7

print(orchard(T,m))
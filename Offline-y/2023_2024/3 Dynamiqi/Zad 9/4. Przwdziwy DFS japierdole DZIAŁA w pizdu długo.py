def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

def trip(M):

    def szukanie_min_val_gdzie_nie_bylem(G):
        min_val = float('inf')
        coords = None

        for row in range(all_rows):
            for col in range(all_cols):
                if M[row][col] < min_val and been_here[row][col] == False:
                    coords = [row,col]
                    min_val = M[row][col]

        return coords

    def DFS(row,col):

        been_here[row][col] = True
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        nowehere_to_go = True
        for y, x in directions:

            if 0 <= row + y <= all_rows - 1 and 0 <= col + x <= all_cols - 1 and \
                    been_here[row + y][col + x] == True and \
                    M[row + y][col + x] > M[row][col] and\
                    paths[row + y][col + x] > paths[row][col]:

                    print(f'jestem w row {row},  col {col}  i nadpisuje z row {row + y} col  {col + x}')
                    print(f'zmieniam na {paths[row + y][col + x] + 1} z  { paths[row][col]}')
                    paths[row][col] = paths[row + y][col + x] + 1

            elif 0 <= row + y <= all_rows - 1 and 0 <= col + x <= all_cols - 1 and \
                    been_here[row + y][col + x] == False and \
                    M[row + y][col + x] > M[row][col]:

                nowehere_to_go = False
                DFS(row + y,col + x)
                paths[row][col] = max(paths[row + y][col + x] + 1,paths[row][col])

        if nowehere_to_go == True and paths[row][col] == 0:
            paths[row][col] = 1

        return paths[row][col]






    all_rows = len(M)
    all_cols = len(M[0])
    been_here = [[False for _ in range(all_cols)] for _ in range(all_rows)]
    max_path = 0
    cords = szukanie_min_val_gdzie_nie_bylem(M)
    paths = [[0 for _ in range(all_cols)] for _ in range(all_rows)]


    while cords != None:
        row, col = cords

        max_path = max(max_path, DFS(row, col))
        cords = szukanie_min_val_gdzie_nie_bylem(M)

        print_straight(paths)
        print('')

    return max_path

M = [ [7,6,5,12],
[8,3,4,11],
[9,1,2,10] ]

M_1 = [[108, 110, 82, 87, 107],
[128, 98, 99, 33, 113],
[114, 5, 115, 32, 19],
[106, 126, 95, 7, 18],
[76, 70, 77, 71, 52]]

print_straight(M_1)
print('')
print(trip(M_1))
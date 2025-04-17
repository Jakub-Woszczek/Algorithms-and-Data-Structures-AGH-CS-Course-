def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

Maze = [ "....",
    "..#.",
    "..#.",
    "...." ]
Maze_2 = ["...#.",
          ".#...",
          "..##.",
          ".....",
          ".#..."]
Maze_test = ['....#...##','...#....##','#.........','.......#..','.......##.','...#....#.','#....#....','##.....#.#','..........','......#...']
Maze_test_3 = ['........#.#....##...', '..................#.', '....#.........##..##', '..#...#..#...#....#.', '........###..#..###.', '..#.#..##....#..#.#.', '#.....#...#.#.#.....', '..#..##......#...###', '.......###.........#', '#.......#..........#', '.#.#..##.#.#.#..#...', '.##..#........#.##.#', '....###...........#.', '........#......#....', '#..............#....', '.#..#......#......#.', '..#................#', '.......#..#.#......#', '.#...............#.#', '#......#....#...#...']
Maze_test_1 = ['......', '#..#..', '.#..#.', '##..#.', '......', '......']
Maze_test_2 = ['....#...##', '...#....##', '#.........', '.......#..', '.......##.', '...#....#.', '#....#....', '##.....#.#', '..........', '......#...']
L_2 = ['....#...##', '...#....##', '#.........', '.......#..', '.......##.', '...#....#.', '#....#....', '##.....#.#', '..........', '......#...']

def MazeFucking_Runner(L):
    # Stworzę tablice dynamiczną z 0 - komnatami i None - niedostępnymi ლ(╹◡╹ლ)
    n = len(L[0])  # Długość wiersza
    m = len(L)  # Liczba wierszy
    DQ = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if L[i][j] == '#':
                DQ[i][j] = None

    quo_vadis = [[[0, 0, 0] for _ in range(n)] for _ in range(m)]
    quo_vadis[0][0] = [1, 1, 0]  # Ustawiam że może wejść w prawo albo w dół

    i = 1
    while i < m and DQ[i][0] != None:
        DQ[i][0] = DQ[i - 1][0] + 1
        quo_vadis[i][0][0] = 1
        i += 1

    for col in range(1, n):
        seed = 0
        if DQ[0][col] != None:
            if DQ[0][col - 1] != None:
                DQ[0][col] = DQ[0][col - 1] + 1
                quo_vadis[0][col][1] = 1

        for row_down in range(1, m):
            if DQ[row_down][col] != None and (
                    quo_vadis[row_down][col - 1] != [0, 0, 0] or quo_vadis[row_down - 1][col] != [0, 0, 0]):
                if DQ[row_down - 1][col] != None and DQ[row_down][col - 1] != None:  # Istnieje góra i lewo
                    if DQ[row_down - 1][col] == DQ[row_down][col - 1]:  # Są takie same
                        DQ[row_down][col] = DQ[row_down][col - 1] + 1
                        quo_vadis[row_down][col] = [1, 1, 0]  # Mógł przyjść z obydwóch kierunków
                    else:  # Są różne
                        DQ[row_down][col] = max(
                            DQ[row_down - 1][col] + 1,  # Góra
                            DQ[row_down][col - 1] + 1  # Lewo
                        )
                        # WYbieram kierunek skąd przyszedł
                        chosen = 0 if DQ[row_down][col] == DQ[row_down - 1][col] + 1 else 1
                        quo_vadis[row_down][col][chosen] = 1
                elif DQ[row_down - 1][col] == None and DQ[row_down][col - 1] == None:  # Obydwa są Nonami
                    DQ[row_down][col] = 0
                elif DQ[row_down - 1][col] == None and DQ[row_down][col - 1] != None:  # Góra to None
                    DQ[row_down][col] = DQ[row_down][col - 1] + 1
                    quo_vadis[row_down][col][1] = 1
                else:  # Lewo to None
                    DQ[row_down][col] = DQ[row_down - 1][col] + 1
                    quo_vadis[row_down][col][0] = 1

        for row_up in range(m - 2, -1, -1):
            if DQ[row_up][col] != None:
                if DQ[row_up + 1][col] != None and (
                        quo_vadis[row_up + 1][col][1] == 1 or quo_vadis[row_up + 1][col][2] == 1):
                    DQ[row_up][col] = max(
                        DQ[row_up][col],
                        DQ[row_up + 1][col] + 1
                    )
                    quo_vadis[row_up][col][2] = 1
                elif DQ[row_up][col - 1] != None and DQ[row_up + 1][col] == None and DQ[row_up][col - 1] != 0 and quo_vadis[row_up][col] != [0,0,0]:
                    seed = DQ[row_up][col - 1] + 1
                if seed > DQ[row_up][col] and (quo_vadis[row_up-1][col][1] == 1 or quo_vadis[row_up-1][col][2] == 1):
                    DQ[row_up][col] = seed
            else:
                seed = 0
            seed += 1

    return DQ

T = MazeFucking_Runner(L_2)

for i in range(len(T)):
    for j in range(len(T)):
        if T[i][j] == None:
            T[i][j] = '_'


# print(MazeFucking_Runner(Maze_2))

# Oblicz maksymalną szerokość każdej kolumny
column_widths = [max(len(str(T[i][j])) for i in range(len(T))) for j in range(len(T[0]))]

# Wypośrodkuj kolumny
for row in T:
    row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
    print(row_str)



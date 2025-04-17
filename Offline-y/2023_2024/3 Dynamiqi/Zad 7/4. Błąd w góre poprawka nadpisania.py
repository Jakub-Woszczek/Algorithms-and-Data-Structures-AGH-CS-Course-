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
Maze_test_2 = ['........#.#....##...', '..................#.', '....#.........##..##', '..#...#..#...#....#.', '........###..#..###.', '..#.#..##....#..#.#.', '#.....#...#.#.#.....', '..#..##......#...###', '.......###.........#', '#.......#..........#', '.#.#..##.#.#.#..#...', '.##..#........#.##.#', '....###...........#.', '........#......#....', '#..............#....', '.#..#......#......#.', '..#................#', '.......#..#.#......#', '.#...............#.#', '#......#....#...#...']

def MazeFucking_Runner(L):

    # Stworzę tablice dynamiczną z 0 - komnatami i None - niedostępnymi ლ(╹◡╹ლ)
    n = len(L)
    DQ = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                DQ[i][j] = None

    # Uznałem ze stowrze tablice gdzie każdej możliwej komancie przypisze krotke [0,0,0] odpowiadającej czy dostał się
    # tam z Góry,Lewa czy z Dołu. 1-True 0-False
    quo_vadis = [[[0,0,0] for _ in range(n)] for _ in range(n)]
    quo_vadis[0][0] = [1,1,0] # Ustawiam że może wejść w prawo albo w dół
    # [0, 0, 0, 0]
    # [0, 0, None, 0]
    # [0, 0, None, 0]
    # [0, 0, 0, 0]

    # Teraz zrobie dynamiqa

    # # Pierwsza pętelka w dół
    # for i in range(1,n):
    #     if DQ[i-1][0] != None and DQ[i][0] != None and quo_vadis[i][0][0] == 1:
    #         DQ[i][0] = i
    #         quo_vadis[i][0][0] = 1

    # Alternatywna pierwsza pętelka w dół
    i = 1
    while i < n and DQ[i][0] != None:
        DQ[i][0] = DQ[i-1][0] + 1
        quo_vadis[i][0][0] = 1
        i += 1

    # Teraz spróbóje przechodzić przez kazdą kolumnę w doł i i w góre i aktualizować ilość komnat

    for col in range(1,n):
        # Aktualizeuje w dół ( Pierwsze okienko )
        if DQ[0][col] != None:
            if DQ[0][col - 1] != None:
                DQ[0][col] = DQ[0][col - 1] + 1
                quo_vadis[0][i][1] = 1

        for row_down in range(1,n):

            if DQ[row_down][col] != None and (quo_vadis[row_down][col-1] != [0,0,0] or quo_vadis[row_down-1][col] != [0,0,0]):

                if DQ[row_down-1][col] != None and DQ[row_down][col-1] != None: # Istnieje góra i lewo
                    if DQ[row_down-1][col] == DQ[row_down][col-1]: # Są takie same
                        DQ[row_down][col] = DQ[row_down][col-1] + 1
                        quo_vadis[row_down][col] = [1,1,0] # Mógł przyjść z obydwóch kierunków
                    else: # Są różne
                        DQ[row_down][col] = max(
                            DQ[row_down - 1][col] + 1,  # Góra
                            DQ[row_down][col - 1] + 1  # Lewo
                        )
                        # WYbieram kierunek skąd przyszedł
                        chosen = 0 if DQ[row_down][col] == DQ[row_down - 1][col] + 1 else 1
                        quo_vadis[row_down][col][chosen] = 1

                elif DQ[row_down-1][col] == None and DQ[row_down][col-1] == None: # Obydwa są Nonami
                    DQ[row_down][col] = 0

                elif DQ[row_down-1][col] == None and DQ[row_down][col-1] != None: # Góra to None
                    DQ[row_down][col] = DQ[row_down][col-1] + 1
                    quo_vadis[row_down][col][1] = 1

                else: # Lewo to None
                    DQ[row_down][col] = DQ[row_down - 1][col] + 1
                    quo_vadis[row_down][col][0] = 1

        # Aktualizuje w góre
        possible_seed = None # To jest po to by rozwiązać edge case

        for row_up in range(n-2,-1,-1):
            if DQ[row_up][col] == None:
                possible_seed = None
            elif (DQ[row_up][col] != None and
                DQ[row_up + 1][col] == None and
                DQ[row_up][col-1] != None):
                possible_seed = DQ[row_up][col-1] + 1


            elif (DQ[row_up][col] != None and
                DQ[row_up + 1][col] != None and # Czy Dolny istnieje
                (quo_vadis[row_up + 1][col][1] == 1 or quo_vadis[row_up + 1][col][2] == 1) ): # Czy można dość do dolnego z lewej strony

                DQ[row_up][col] = max(
                    DQ[row_up][col],
                    DQ[row_up+1][col] + 1,
                )
                if possible_seed != None:
                    DQ[row_up][col] = max(
                        DQ[row_up][col],
                        possible_seed
                    )
                quo_vadis[row_up][col][2] = 1

            elif possible_seed != None:
                possible_seed += 1


    return DQ

T = MazeFucking_Runner(Maze_test_2)
# ◼⬛🔳🔲
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



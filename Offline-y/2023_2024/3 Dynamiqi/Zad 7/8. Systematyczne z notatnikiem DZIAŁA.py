def Maze(L):

    def z_kropek_na_zera(Hash_map):
        n = len(Hash_map)
        Labi = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if Hash_map[i][j] == '#':
                    Labi[i][j] = None

        return Labi
    def wypelnianie_niedostepnych(Labi):
        from collections import deque
        def Wypelnij_niedostepne_Nonami_lewy_gorny(Labirynt):
            n = len(Labirynt)
            m = len(Labirynt[0]) if n > 0 else 0

            # BFS
            queue = deque([(0, 0)])
            while queue:
                x, y = queue.popleft()
                if Labirynt[x][y] == 0:
                    Labirynt[x][y] = 'V'  # 'V' oznacza, że komórka była odwiedzona

                    # Sprawdzanie sąsiadów
                    for dx, dy in [(0, 1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and Labirynt[nx][ny] == 0:
                            queue.append((nx, ny))

            # Oznaczanie niedostępnych komórek jako None
            for i in range(n):
                for j in range(m):
                    if Labirynt[i][j] == 0:
                        Labirynt[i][j] = None
                    elif Labirynt[i][j] == 'V':
                        Labirynt[i][j] = 0

            return Labirynt

        def Wypelnij_niedostepne_Nonami_prawny_dolny(Labirynt):
            n = len(Labirynt)
            m = len(Labirynt[0]) if n > 0 else 0

            # BFS starting from T[n-1][n-1]
            queue = deque([(n - 1, n - 1)])
            while queue:
                x, y = queue.popleft()
                if Labirynt[x][y] == 0:
                    Labirynt[x][y] = 'V'  # 'V' oznacza, że komórka była odwiedzona

                    # Sprawdzanie sąsiadów
                    for dx, dy in [(0, -1), (-1, 0), (1, 0)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and Labirynt[nx][ny] == 0:
                            queue.append((nx, ny))

            # Oznaczanie niedostępnych komórek jako None
            for i in range(n):
                for j in range(m):
                    if Labirynt[i][j] == 0:
                        Labirynt[i][j] = None
                    elif Labirynt[i][j] == 'V':
                        Labirynt[i][j] = 0

            return Labirynt

        Labi = Wypelnij_niedostepne_Nonami_lewy_gorny(Labi)
        Labi = Wypelnij_niedostepne_Nonami_prawny_dolny(Labi)

        return Labi

    DQ = z_kropek_na_zera(L) # Zamieniam na zaera i None
    # DQ = wypelnianie_niedostepnych(DQ) # Wypełniam niedostępne miejsca None-ami
    n = len(L)

    ### ALGORYTM ###

    #___________ PIERWSZA KOLUMNA W DÓŁ __________#

    row = 1
    while row < n and DQ[row][0] != None:
        DQ[row][0] = DQ[row - 1][0] + 1
        row += 1



    # ___________ GŁÓWNA PĘTLA DLA KAŻDEJ KOLUMNY __________#

    for col in range(1,n):

        # ___________ PRZEPISANIE LEWEJ STRONY + 1 __________#
        for down_row_1 in range(n):
            if DQ[down_row_1][col] != None and DQ[down_row_1][col-1] != None:
                DQ[down_row_1][col] = DQ[down_row_1][col-1] + 1


        # ___________ NJADŁUŻSZA ŚCIEŻKA W DÓŁ __________#
        for down_row_path in range(1,n):
            if DQ[down_row_path][col] != None and DQ[down_row_path-1][col] != None:
                DQ[down_row_path][col] = max(DQ[down_row_path][col],DQ[down_row_path-1][col]+1)


        # ___________ NJADŁUŻSZA ŚCIEŻKA W GÓRE __________#
        seed = 0
        for up_row in range(n-1,-1,-1):

            if DQ[up_row][col] == None:
                seed = 0

            else:
                if seed != 0:
                    seed += 1

                if DQ[up_row][col - 1] != None:
                    seed = max(seed,DQ[up_row][col - 1] + 1)

                DQ[up_row][col] = max(seed,DQ[up_row][col])


    return DQ

def dodawanie_map():
    T = []
    Maze_my_1 = ["....",
                 "..#.",
                 "..#.",
                 "...."] # 0

    Maze_my_2 = ["...#.",
                 ".#...",
                 "..##.",
                 ".....",
                 ".#..."] # 1

    Maze_test_0 = ['....', '..#.', '..#.', '....'] # 2
    Maze_test_1 = ['......', '#..#..', '.#..#.', '##..#.', '......', '......'] # 3
    Maze_test_2 = ['....#...##', '...#....##', '#.........', '.......#..', '.......##.', '...#....#.', '#....#....',
                   '##.....#.#', '..........', '......#...'] # 4
    Maze_test_3 = ['........#.#....##...', '..................#.', '....#.........##..##', '..#...#..#...#....#.',
                   '........###..#..###.', '..#.#..##....#..#.#.', '#.....#...#.#.#.....', '..#..##......#...###',
                   '.......###.........#', '#.......#..........#', '.#.#..##.#.#.#..#...', '.##..#........#.##.#',
                   '....###...........#.', '........#......#....', '#..............#....', '.#..#......#......#.',
                   '..#................#', '.......#..#.#......#', '.#...............#.#', '#......#....#...#...'] # 5
    Maze_test_4 = ['..#.........#......#..........#.......#.#.........',
                   '...........##..#....##.#.......#.#....#.#.#.#.....',
                   '.#.#.......##.........#..#..#.#..#.....#...#......',
                   '......#...#....#....................#......#...#..',
                   '....#.....#...............#..#.#......##...#....#.',
                   '....#.....#...##..##..#....#........#..........#..',
                   '#......#...............#...#..###..#......#......#',
                   '.....#.#.....#.....#............#.#.#........#...#',
                   '....#.....#.....#....#....#..#..............###...',
                   '#..##...##........##..#...#................#####..',
                   '.#..........##...............#.............##..#..',
                   '..........#..#....#...##.......##.#.#......#......',
                   '..#.#.#....#........#..##....#...##...............',
                   '...#..........#.#.##.#.......##..#....#####.......',
                   '...#........#.#...#..###..#..#..#........##..#....',
                   '.....##......#...##.#.#.........#...#...#.....##..',
                   '.#..#................#.#..#.#...##.#.....##...#...',
                   '........#.#....##....#..###.#.......#....#.#.#...#',
                   '.#.....#.......#.........#.#.........##.#....#....',
                   '..#.##.....#...........#.....##............#.....#',
                   '..#..........#.......##.#.#...........#..#........',
                   '.#####.##.#.........#..............##..#..#.#.##..',
                   '...#........#...###..#................#...........',
                   '.......................#.....#...#................',
                   '#.#.....................#.#........#...........#..',
                   '.####..#...#.#.#.....#..........#.#.....#.#.##...#',
                   '#.....##..#..#..#...#.#........#.#......#.#.......',
                   '........####.........................#.......#....',
                   '......##...##.#.......#.#.......##...#...#......#.',
                   '...#........#..#................#.#..#.#..........',
                   '................##.#..#........#..............#...',
                   '.#....#............#...#...##.#..#.#.#............',
                   '..#..#..#..#..#..#...#.##.#.....#..........#......',
                   '#....#.....#..#.##.#.###......#....#.#.........#..',
                   '......#........#..##....#..........#...#..........',
                   '#..........#........#....#...#.....###.#..#.#..#..',
                   '............#....#.##......#.#..........#.#.....#.',
                   '#..#.#.##...............#.......#.##...##.#....#..',
                   '.#....##....#.........#...#.#.....##.#.....##...#.',
                   '#..........#........#..#.#.#...#...#....#.........',
                   '.#....#....#...##..........#.......#......#.......',
                   '..#...#.....#..#.....#.........#...##.#....#.#....',
                   '......#.........#........##...#..#.#.#..#.....#...',
                   '...##....#....##.##...#..#..####.....##......#.###',
                   '..#........#......#.............#......#...#......',
                   '#...........#....#..#..###......#...#..###..#.....',
                   '..#.#.......#.#............#...#......#...........',
                   '.#....#.........#..#..#...#....##.#.#..#..#.......',
                   '#......#..#.#..##......#...#..#.###.......#...#...',
                   '...#...##..#.......................##....#.....#..'] # 6
    Maze_test_5 = [
        '.#...#.#.........##.#..#.....#.#.#...#....#...#.....#...............##...#....###.##......#.#.#.....',
        '.......#..##.............#....#...##..#....#........#.....##......#..............#........#.#..#..##',
        '##........#............#............##..##......#.#...###.#......##......#..##.#..#....#..#.........',
        '#...........##.#............#...#.#.##......#......#................##...#......##.........#......#.',
        '............#...##.....#....#....#............#.......#.....#.......##....#.#.......##.#.###......#.',
        '...........#..........#.#.#...#...#..........#..#........#..#......##...........####..........##....',
        '......#..#............#..#...##...##...##......#.#......#..#..###........###..###..........#..#.....',
        '#.......#.................#.........#.#.........###......#...#.....##.#.........#.........#...#..#..',
        '.........#...#..#.#.#..#.#..........#....#........#....#......#.......#..##.....#.#..........#......',
        '....##..#...............##...............#.......#..#..#..............##...#...##........#.#....#...',
        '..........#...#...........#.#....#....#.............##.###.......##.....#.#.....#.........#..##....#',
        '............#........#.#......#.#..#..#...............#....##.....#....#.......###....#..#....###.#.',
        '...#...#..#.##..#.........#.#.#...........#......#......#.#...........................#.##..........',
        '....#..#...#....#.#.......##..#.##.#.......#.#.......#.........#.#.#..##.....#.#....#....#........#.',
        '...#..........#.....#..#.............#.......#........#.......#.............#.......#.#........#..#.',
        '.....#..#.#..#.....####...#.............#..#...#........#......#....#.#..#...#...#......##......#..#',
        '......##.......##......#....#...#.......................#...#.....................#...#.#...........',
        '.#.......##.#..#........#.#............#.........#......#................#..#....#.#....#.....#.....',
        '.......#..#.##.#.....#..#......#....#...#.....##.......#...#.#....#......#..##.#.....##.##..........',
        '..#.......#............#.........#..##.....#.......#...#...##..............#.#....#...............#.',
        '............#..........#....#.....#.....##...........................#...#.#..#....##....#..........',
        '.#.#........#...........#...#.....#......#.#..##.....#.#.......#.#.......##.#....##...#.#..#.....#..',
        '.....##......#....#...............................#..........##.#..#.....####....#...#.#.......#.#..',
        '.#.......................#.............#...#.......#..#........#..............##...............#....',
        '........#.....##..#..#....#...#.#...#...#.....#.#.##..#.........#......##.......#.....#...#.#...#...',
        '.........#..#.....#..##..#..........#.#............#...#........#.................#......###...##...',
        '.....##....##...................#.#...#.#.##.......#...#.........#.........#..#.......#......#......',
        '..................#...##...#...#.#......#..#.......###............#.....#....#.#....................',
        '..#.#.......#.....##....##......#..#..#.........#.....#...............#..#.#...............##..#.###',
        '.#...........##...............#...##......................#.#....#.#....#.#........##.#.#........#..',
        '.##......#.#.......#..#..#......#.........#....#.#......#.###....#......#.................#.##......',
        '#..#......#.........##..........#.....#..#.#.#........#.#.....#.##...##..#....#.....#.....#.#.##....',
        '...#........##.....#..#............##.#.##.......#....##.###..#.....#.......#......##....#.#.##..#..',
        '.......#.##....#......#..#....#................#....#....#.....#.....##...............###.......#...',
        '..#...#.....##...#.......#.......#.##.#...#.#.#........#..#......#..###.........#......#.##........#',
        '........#........##......#.......#....#.###.###.....#..................#...#...##...........##...#..',
        '........#.#.........###....#......##...#..#......##..#.......#...#....##.##..#...........#...##.#...',
        '........##....##...##.....#....#...#.......#..............#...............#.........#.....#..##.....',
        '.#.#......#...##....#...##.##.#....#.....#........#.#..#...#.......#......#.##.....#.......#....#..#',
        '#..........#..#...............#.#..##..#...#.###..#..........#...............#......#.#.............',
        '......#...#..........#..#.....##...#.#.##......##.#.#...#..##....#.....#.#.....#.....#....#.........',
        '##.##...#..................##.#.#.#..#.#........#.#.....#..#...###.........##.#.........#...#....#..',
        '#..........#...#....#...........#.....#.......#..........#...#.##..###.......................#......',
        '.....#.......####..#...#..#........###...............#.....#..##...........#.#...#.#...#.#...#......',
        '.........#.#........#...##......#...#.#....#..#.......#.#.#.....#..........#.................#.....#',
        '...................#.......#.#......#..#..#.........#..#.#.#......#.#.................#.#....#......',
        '........#....###...#...##.#.........##.#...#.......#......#..#.......#...#.#..............##......##',
        '..........#....#.......#..#.####............#..#......##..#......#....#.....#.......#.#.............',
        '##....##.........#.#......#..#.#.#....#............#.....#.......#.....................#.....#......',
        '........#.......#.....#.......##..##.#...#................#....##...##...........##..###.#...#......',
        '.......#.#.........#.#..#.#.#...#.#...#..#....#.#......#..........#........................#........',
        '#.##........#...................#...#....#.....#....#....#.#.#..##.........#...##.#........##......#',
        '...##.#.....#..................#.....#.......#.#.......#..............#....##..#..........#.........',
        '...........#............#.#............#........#....#....#....#.#...#.#.........#..#.#.......#.....',
        '......#.....#.#.......#.#..#......#......#..#..#.......#......#..........##.....#...#........#......',
        '..#...#....#...###...#............##...#..#...#......##....#..#.#...#............##..#....#....###..',
        '..#..#.......................#............##......#........#...................#.#.##...#..#......#.',
        '...#.#............###......##....##..#.#..#.............#..#..#...#.........##........#.............',
        '#.....#...#.#....#....#...#.......#.....#..#............#.....##...#.....#................#...#..#..',
        '...#........#......#...........#.......#.##.......#...#.....#..#.....................#..#.#......#..',
        '.................#..#......#....#.........#....##..#........#...........................##.#.....#..',
        '.#...#...#..............#....##..#..#......##.#............#..............#.#.......#.##....#...#...',
        '...##.#...#...#...........##.....#..#..#.....##.....#....#...#...##.#...#..#.......#......####....#.',
        '......##.........#...#.....#...##............##.............#...#........##.....#..#.##.#.##......#.',
        '.#.....#.##....................#..#.........#..#...#........#..#............#.......#..........#..##',
        '...............#.....#..#..........#...........#...#..#..#......##..#.#...............#..#..#...#...',
        '#.........#.#..........##.##..#.#...#....#............##...#..................#.#...#...#...........',
        '...#.......###......#............#.....#.#....#..........#...#..#........#####....#...#....#.#..#...',
        '....##....#......###.#.........#.....#.#........#.#....#...#.....................#...#..#....#.##..#',
        '.........###...#.##...#......#.....#..#.......#.##........#.....#.....##.#.#...##.#.#....#####..#...',
        '..#......#......#....##.....#.#.....#.#..#.....#.#.#.......#...#..#....#......#...#.#...###.#....#..',
        '.......#......#....#.##..........#.........##............###...#......#....###.......##....##.......',
        '.####....#..#..#.#..........#..#...#..#..##..#.#........#....#........#......#..#.......#...........',
        '.#.......#.........#...#.....#..............#..#......##........#..........#.........##........#....',
        '.#....#...........###.#.....#..#...##........#.....#.#..#...#.#...........................#.#.......',
        '##.....##...#.#...................#...#.#..##.#..#.........##..##.#....#....#.......#..#......#.....',
        '#...#.#.....#.##........#........#.......#..#...##..#......#.......#......#...##.#...##......##....#',
        '##.#...#.#.#....##....#.#........#....#....##..#.....#..##..#.#.................#.......#.........#.',
        '.....#..##..#..#....#.......#...#....#...........#.....#........#................#...#..###..#.#.#..',
        '.#...........#....#....#...#.....#..#....#.......#..#.#...#.#...............##................#...#.',
        '#.#..#...#.....##....#.#..........#..#...#........##....#..#..#..#.#..#.....#..##.....###...#...#..#',
        '...#....#.......#............#...#.....#..........#.....#.....##...##.##..........#...##...#......#.',
        '..#..#..........##...#.#.....##.#..#.#.##......#..........#.....#......#..#..#...#.#.......#.......#',
        '.....#..#..#..#.#.#..#.....#.........#.##.##......#....#....#.##.........#..........#..##...#...#.#.',
        '.....##....#.........#.....#..#......#..#...............#..........#..........#..###...#....#.......',
        '.......##...#.......##.................#..........#..#....##..#............#....#.#.###....#..#....#',
        '......#..#.......#.........#.....#..#...........#..#.####........#..#..#.....##......#..........#...',
        '.....#.......#..###.......#..#..........####..........#.......#.....#....#.#......#...##....#..#....',
        '.......#.......#....#....#..#............#........#......##...#...........#.#.##....#...#...........',
        '#.#..#..#.......#..####.#..#.....#.#.......#.....##...#.#..........#..##....##..#........#..#...#...',
        '....................#...#.##.......##.#.......#.#.##.........#.#...##.##..........#....#.........#.#',
        '#.................####.......#.##..##.....#.#...##....##...#..........##.....##...#..#....#.#.......',
        '.....##.......#................#.#..................#..#..#......#.......#...#.....#...#.....#......',
        '.........###...#.....#........#....#.#....#.................#.........#..#..........#...#.........#.',
        '........#.....#....#.......#.#...#............##..#.#..#.#.......#.#....#...##.........#..........#.',
        '......#.........#.#.#.....#..##..#......#......#...#...........#..........#...............#..#.#.#..',
        '....###..#.....................##....#.####............##................#.............#...#........',
        '........#...#..##...###..#.#..............#...###..##...#........#...#..###..........#....#.##.#.#..',
        '.#......#.....................#..#..........#.#..#......#...#......#.......#.....###..##..###.#.....',
        '..#.#.#.....#...#...#.#......#....#....#...........#.........#.......#...#...##.#..#........#....#..'] # 7
    T.append(Maze_my_1)
    T.append(Maze_my_2)
    T.append(Maze_test_0)
    T.append(Maze_test_1)
    T.append(Maze_test_2)
    T.append(Maze_test_3)
    T.append(Maze_test_4)
    T.append(Maze_test_5)

    return T

def tester(index_Hash_mapy):
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

    T = dodawanie_map()
    Hash_mapa = T[index_Hash_mapy]
    print_straight(Hash_mapa)
    print()
    print_straight(Maze(Hash_mapa))

tester(5)


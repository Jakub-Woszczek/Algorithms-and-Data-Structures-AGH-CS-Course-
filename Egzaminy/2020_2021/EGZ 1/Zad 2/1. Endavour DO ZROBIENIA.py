def print_2d_array(arr):
    # Zamień zera na None
    arr = [[None if num == 0 else num for num in row] for row in arr]

    # Znajdź maksymalną długość dla każdej kolumny
    max_lengths = [max(len(str(item)) for item in column) for column in zip(*arr)]

    for row in arr:
        for num, length in zip(row, max_lengths):
            if num is None:
                print(f'{"#".ljust(length)}', end=' ')
            else:
                print(f'{num}'.ljust(length), end=' ')
        print()


def process_and_print_maze_and_times(maze, times):
    # Zamiana inf na 0 w tablicy czasów dotarcia
    times = [[0 if cell == float('inf') else cell for cell in row] for row in times]

    # Funkcja do wyśrodkowania i wyświetlania labiryntu
    def print_centered_maze(maze):
        max_length = len(maze[0])
        for row in maze:
            print(row.center(max_length))

    # Funkcja do wyświetlania tablicy czasów dotarcia
    def print_times(times):
        # Oblicz maksymalną długość liczby w tablicy
        max_length = max(len(str(cell)) for row in times for cell in row)
        for row in times:
            print(' '.join(f'{cell:>{max_length}}' for cell in row))

    # Wyświetlenie wyśrodkowanego labiryntu
    print("Wyśrodkowany labirynt:")
    print_centered_maze(maze)

    # Wyświetlenie wyśrodkowanej tablicy czasów dotarcia
    print("\nWyśrodkowana tablica czasów dotarcia:")
    print_times(times)

def robot( L, A, B):
    T_of_times = [[float('inf') for _ in range(len(L[0]))] for _ in range(len(L))]

    from queue import Queue

    row_org,col_org = A
    Q = Queue()

    if L[row_org-1][col_org] == ' ':
        Q.put((row_org-1,col_org,0,45 + 60))

    if L[row_org][col_org+1] == " ":
        Q.put((row_org,col_org+1,1,0 + 60))

    if L[row_org+1][col_org] == ' ':
        Q.put((row_org+1,col_org,2,45 + 60))

    if L[row_org][col_org-1] == ' ':
        Q.put((row_org,col_org-1,3,90 + 60))



    while not Q.empty():

        row,col,direction,curr_time = Q.get()

        if direction == 0:
            nr_odc = 2
            while L[row][col] != 'X':
                if T_of_times[row][col] <= curr_time:
                    break
                T_of_times[row][col] = curr_time

                if nr_odc < 3:
                    if nr_odc == 1:
                        curr_time += 60
                    elif nr_odc == 2:
                        curr_time += 40
                else:
                    curr_time += 30

                if L[row][col + 1] == " ":
                    Q.put((row,col + 1, 1, curr_time +45 + 60))

                nr_odc += 1
                row -= 1



        elif direction == 1:  # Ruch w prawo
            nr_odc = 2
            while col < len(L[0]) and L[row][col] != 'X':
                if T_of_times[row][col] <= curr_time:
                    break
                T_of_times[row][col] = curr_time
                curr_time += 60 if nr_odc == 1 else 40 if nr_odc == 2 else 30
                if row + 1 < len(L) and L[row + 1][col] == " ":
                    Q.put((row + 1, col, 2, curr_time + 45 + 60))
                nr_odc += 1
                col += 1

        elif direction == 2:  # Ruch w dół
            nr_odc = 2
            while row < len(L) and L[row][col] != 'X':
                if T_of_times[row][col] <= curr_time:
                    break
                T_of_times[row][col] = curr_time
                curr_time += 60 if nr_odc == 1 else 40 if nr_odc == 2 else 30
                if col - 1 >= 0 and L[row][col - 1] == " ":
                    Q.put((row, col - 1, 3, curr_time + 45 + 60))
                nr_odc += 1
                row += 1

        elif direction == 3:  # Ruch w lewo
            nr_odc = 2
            while col >= 0 and L[row][col] != 'X':
                if T_of_times[row][col] <= curr_time:
                    break
                T_of_times[row][col] = curr_time
                curr_time += 60 if nr_odc == 1 else 40 if nr_odc == 2 else 30
                if row - 1 >= 0 and L[row - 1][col] == " ":
                    Q.put((row - 1, col, 0, curr_time + 45 + 60))
                nr_odc += 1
                col -= 1



        process_and_print_maze_and_times(L,T_of_times)


L=          [ "XXXXXXXXXX", # 0
              "X        X", # 1
              "X  XXXXXXX", # 2
              "X        X", # 3
              "X XXXXXX X", # 4
              "X        X", # 5
              "XXXXXXXXXX", # 6
            ]

robot(L,(3,1),90)

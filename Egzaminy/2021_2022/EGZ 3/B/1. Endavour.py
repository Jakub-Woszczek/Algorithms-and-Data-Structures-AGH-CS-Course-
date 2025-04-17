def print_2d_array(array):
    # Oblicz szerokość największego elementu w tablicy, aby ustalić szerokość kolumn
    col_width = max(len(str(element)) for row in array for element in row)

    for row in array:
        # Drukuj każdy element w wierszu, wyrównując go do prawej strony z szerokością kolumny
        print(" ".join(f"{str(element):>{col_width}}" for element in row))
def print_straight(T):
    # Zamień None na '#'
    formatted_T = [[('#' if item is None else item) for item in row] for row in T]

    # Oblicz maksymalną szerokość każdej kolumny
    column_widths = [max(len(str(formatted_T[i][j])) for i in range(len(formatted_T))) for j in range(len(formatted_T[0]))]

    # Wypośrodkuj kolumny
    for row in formatted_T:
        row_str = " ".join(f"{str(row[col]).rjust(column_widths[col])}" for col in range(len(row)))
        print(row_str)

# Algos polega na tym ze przepisuje jedno w prawo poźniej na osobnych
# tablicach szukam max path w góre i w dół poźniej biore max z tego

def maze( L ):
    n = len(L)
    Down = [[-1 for _ in range(n)] for _ in range(n)]
    Up = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if L[i][j] == '#':
                Down[i][j] = None
                Up[i][j] = None

    i = 0
    while (i < n) and Down[i][0] != None:  # Robie pierwszą kolumne
        Down[i][0] = i
        i += 1

    for col in range(1, n): # Dla każdej kolumny

        for row in range(0, n): # Przepisuje jak można w prawo i dodaje jeden
            if Down[row][col - 1] != None and Down[row][col] != None and Down[row][col - 1] != -1:

                Down[row][col] = Down[row][col - 1] + 1
                Up[row][col]  =  Down[row][col - 1] + 1

        for row in range(1, n): # Szukam maxa w dół
            if Down[row - 1][col] != None and Down[row][col] != None and Down[row - 1][col] != -1:

                Down[row][col] = max(Down[row][col], Down[row - 1][col] + 1)

        for row in range(n - 2, -1, -1): # Szukam maxa w góre
            if Up[row][col] != None and Up[row + 1][col] != None and Up[row + 1][col] != -1:

                Up[row][col] = max(Up[row][col], Up[row + 1][col] + 1)

        for row in range(n): # Biore maxa z tablicy góra i dół
            if Down[row][col] != None and Up[row][col] != None:

                Down[row][col] = max(Down[row][col], Up[row][col])


    return Down[n - 1][n - 1]

L = ['....','..#.','..#.','....']
L_1 = ['......', '#..#..', '.#..#.', '##..#.', '......', '......']
L_2 = ['....#...##', '...#....##', '#.........', '.......#..', '.......##.', '...#....#.', '#....#....', '##.....#.#', '..........', '......#...']

maze(L_2)

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

    def aktualizacja_coloru(row,col,new_path_len):

        if childs[row][col] == None:
            paths[row][col] = new_path_len
            return new_path_len

        paths[row][col] = new_path_len
        next_row,next_col = childs[row][col]
        new_len = aktualizacja_coloru(next_row,next_col,new_path_len + 1)

        return new_len

    def DFS(row,col,colour,path_len):

        paths[row][col] = path_len
        max_len = path_len
        been_here[row][col] = True
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        colors[row][col] = colour

        for y,x in directions:

            if 0 <= row + y <= all_rows - 1 and 0 <= col + x <= all_cols - 1 and \
                    been_here[row + y][col + x] == True and\
                    colors[row + y][col + x] == colour and\
                    paths[row + y][col + x] < path_len + 1 and\
                    M[row + y][col + x] > M[row][col]:

                # Tutaj def - aktualizacja
                max_len = max(max_len,aktualizacja_coloru(row + y,col + x,path_len + 1))

            elif 0 <= row + y <= all_rows - 1 and 0 <= col + x <= all_cols - 1 and\
                    been_here[row + y][col + x] == False and\
                    M[row + y][col + x] > M[row][col]: # Ide do następnego gdzie nie byłem

                childs[row][col] = [row + y,col + x]
                max_len = max(DFS(row + y,col + x,colour,path_len + 1),max_len)

        return max_len

    all_rows = len(M)
    all_cols = len(M[0])
    been_here = [[False for _ in range(all_cols)] for _ in range(all_rows)]
    colors = [[0 for _ in range(all_cols)] for _ in range(all_rows)]
    max_path = 0
    cords = szukanie_min_val_gdzie_nie_bylem(M)
    color = 1
    childs = [[None for _ in range(all_cols)] for _ in range(all_rows)]
    paths = [[0 for _ in range(all_cols)] for _ in range(all_rows)]

    while cords != None:

        row, col = cords

        max_path = max(max_path,DFS(row,col,color,1))
        cords = szukanie_min_val_gdzie_nie_bylem(M)
        color += 1

    return max_path

M = [ [7,6,5,12],
[8,3,4,11],
[9,1,2,10] ]


print(trip(M))
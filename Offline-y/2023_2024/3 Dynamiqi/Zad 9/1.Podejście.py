def trip(M):
    max_dfs_len = 0
    def create_sorted_list(M):
        rows = len(M)
        cols = len(M[0])

        # Tworzymy listę z wartościami i ich współrzędnymi
        T = []
        for i in range(rows):
            for j in range(cols):
                T.append((M[i][j], [i, j]))

        # Sortujemy listę według wartości
        T.sort(key=lambda x: x[0])

        return T

    def DFS(row,col,path_len,max_val):

        if M[row][col] > max_val:
            max_val = M[row][col]

        nonlocal max_dfs_len
        if path_len > max_dfs_len:
            max_dfs_len = path_len

        been_here[row][col] = True
        directions = [[-1,0],[0,1],[1,0],[0,-1]]

        for y,x in directions:
            if been_here[row + y][col + x] == False and M[row + y][col + x] > M[row][col]:
                DFS(row + y,col + x,path_len + 1,max_val)

        return None

    # Trzeba zrobić dfs of min wierzchołków póki się nie skończą

    T_sorted_vertexes = create_sorted_list(M) # Krotka = [val,[row,col]]
    all_rows = len(M)
    all_cols = len(M[0])
    all_vertx = all_cols*all_rows

    # Tutaj zaczę DFS
    begining_seed = 0

    been_here = [[False for _ in range(all_cols)] for _ in range(all_rows)]
    while begining_seed < all_vertx:

        val,[row,col] = T_sorted_vertexes[begining_seed]
        if been_here[row][col] == False:
            DFS(row,col,0,0)

        begining_seed += 1

    return max_dfs_len

M = [ [7,6,5,12],
[8,3,4,11],
[9,1,2,10] ]


print(trip(M))




import time

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

    def DFS(row,col,path_len):

        max_len = path_len
        been_here[row][col] = True
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for y,x in directions:
            if 0 <= row + y <= all_rows - 1 and 0 <= col + x <= all_cols - 1 and\
                    been_here[row + y][col + x] == False and\
                    M[row + y][col + x] > M[row][col]:

                max_len = max(DFS(row + y,col + x,path_len + 1),max_len)

        return max_len


    all_rows = len(M)
    all_cols = len(M[0])
    been_here = [[False for _ in range(all_cols)] for _ in range(all_rows)]
    max_path = 0
    flaga = True
    cords = szukanie_min_val_gdzie_nie_bylem(M)

    while cords != None:

        row,col = cords

        max_path = max(DFS(row,col,1),max_path)
        cords = szukanie_min_val_gdzie_nie_bylem(M)


    return max_path

M = [ [7,6,5,12],
[8,3,4,11],
[9,1,2,10] ]


print(trip(M))
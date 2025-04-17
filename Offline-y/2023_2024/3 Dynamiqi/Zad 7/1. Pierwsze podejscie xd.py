Maze = [ "....",
    "..#.",
    "..#.",
    "...." ]

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

    # [0, 0, 0, 0]
    # [0, 0, None, 0]
    # [0, 0, None, 0]
    # [0, 0, 0, 0]

    # Teraz zrobie dynamiqa

    # Pierwsza pętelka w dół
    for i in range(1,n):
        if DQ[i-1][0] != None and quo_vadis[i][0][0] == 1:
            DQ[i][0] = i
            quo_vadis[i][0][0] = 1

    # Teraz spróbóje przechodzić przez kazdą kolumnę w doł i i w góre i aktualizować ilość komnat

    for col in range(1,n):
        # Aktualizuje w dół
        DQ[0][col] = DQ[0][col-1] + 1 if DQ[0][col-1] != None else 0
        for row_down in range(1,n):

            if DQ[row_down][col] != None:
                DQ[row_down][col] = max(
                DQ[row_down - 1][col] + 1 if DQ[row_down - 1][col] is not None else 0,
                DQ[row_down][col - 1] + 1 if DQ[row_down][col - 1] is not None else 0
                )

                if DQ[row_down][col] != 0: 
                    chosen = 0 if DQ[row_down - 1][col] != None and DQ[row_down][col] == DQ[row_down - 1][col] + 1 else 1
                    quo_vadis[row_down][col][chosen] = 1

        # Aktualizuje w góre
        for row_up in range(1,n):
            DQ[row_up][col] = max(
                DQ[row_up+1][col] + 1 if DQ[row_up+1][col] != None and quo_vadis[row_up+1][col][0] == 0 else 0,
                DQ[row_up][col]
            )
            chosen = 0 if DQ[row_up][col] == DQ[row_up + 1][col] + 1 else 1
            quo_vadis[row_up][col] = [1 if i == chosen else 0 for i in range(3)]



    return DQ

T = MazeFucking_Runner(Maze)

for bruh in T:
    print(bruh)
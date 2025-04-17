def dominance(P):
    n = len(P)
    MAX_dominance = 0
    max_y,max_x = 0,0
    for pkt in P:
        x,y = pkt
        max_y = max(max_y,y)
        max_x = max(max_x,x)


    Y_list = [0 for _ in range(max_y+1)]
    DQ = [[0, 0] for _ in range(max_x + 1)]

    for pkt in P:
        x,y = pkt

        Y_list[y] += 1
        DQ[x][0] += 1
        DQ[x][1] = max(DQ[x][1],y)

    for i in range(max_y-1,-1,-1):
        Y_list[i] += Y_list[i+1]

    j = 0

    for i in range(max_x,-1,-1):

        MAX_dominance = max(MAX_dominance,n - Y_list[DQ[i][1]] - j - DQ[i][0] + 1)
        j += DQ[i][0]

    return MAX_dominance


P = [(1,3),
(3,4),
(4,2),
(2,2)]

print(dominance(P))
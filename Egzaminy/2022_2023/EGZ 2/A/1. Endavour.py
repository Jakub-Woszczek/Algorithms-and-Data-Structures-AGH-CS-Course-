def dominance(P):

    ilosc_pkt = len(P)
    MAX_dominance = 0

    max_y,max_x = 0,0

    for pkt in P:
        x,y = pkt

        max_x = max(max_x,x)
        max_y = max(max_y,y)

    Y_amnt = [0]*(max_y+1)
    X_amnt = [0] * (max_x + 1)

    for pkt in P:
        x, y = pkt

        if x < max_x:
            X_amnt[x+1] += 1
        if y < max_y:
            Y_amnt[y+1] += 1



    for i in range(1,max_x+1):
        X_amnt[i] += X_amnt[i-1]
    for i in range(1,max_y+1):
        Y_amnt[i] += Y_amnt[i-1]



    for i in range(min(max_x,max_y)):
        MAX_dominance = max(MAX_dominance,min(X_amnt[i],Y_amnt[i]))

    if max_x < max_y:
        last_x = X_amnt[max_x-1]
        last_y = Y_amnt[max_x-1]
        while i < max_y and last_y < last_x:
            last_y = max(last_y,Y_amnt[i])
            i += 1
        MAX_dominance = min(MAX_dominance,min(last_y,last_x))
    else:
        last_x = X_amnt[max_y - 1]
        last_y = Y_amnt[max_y - 1]
        while i < max_x and last_x < last_y:
            last_x = max(last_x, X_amnt[i])
            i += 1
        MAX_dominance = min(MAX_dominance, min(last_y, last_x))

    return MAX_dominance

P = [(1,3),
(3,4),
(4,2),
(2,2)]

print(dominance(P))


def dominance(P):
    cnt_max = 0
    for i in range(len(P)):
        cnt = 0
        x,y = P[i]

        for i in range(0,i):
            if P[i][0] < x and P[i][1] < y:
                cnt +=1
        for i in range(i+1, len(P)):
            if P[i][0] < x and P[i][1] < y:
                cnt +=1

        if cnt > cnt_max:
            cnt_max = cnt

    return cnt_max

P = [(1,3),
(3,4),
(4,2),
(2,2)]
print(dominance(P))


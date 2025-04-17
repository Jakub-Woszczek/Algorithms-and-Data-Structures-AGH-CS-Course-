def uncool( P ):
    n = len(P)
    for i in range(n):
        P[i].append(i)

    print(P)

    P_sorted = sorted(P, key=lambda x: (x[0],x[1]))

    for i in range(n-1):
        if P_sorted[i][0] != P_sorted[i+1][0] and P_sorted[i][1] < P_sorted[i+1][1]:
            print(f'zwracam:P_sorted[i][0] != P_sorted[i+1][0] : {P_sorted[i],P_sorted[i+1]} ')
            return (P_sorted[i][2],P_sorted[i+1][2])


P =[ [1,3], [6,7], [2,6], [4,6], [1,8], [5,10] ]
print(uncool(P))
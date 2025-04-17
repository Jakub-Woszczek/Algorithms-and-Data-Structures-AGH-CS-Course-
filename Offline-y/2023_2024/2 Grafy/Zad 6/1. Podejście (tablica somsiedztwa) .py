G=[
[0, 1, 3, 0],
[1, 0, 1, 2],
[3, 1, 0, 4],
[0, 2, 4, 0]
]

def jumper(G, s, w):

    # Tworze tablice somsiedztwa
    L_soms = [[] for _ in range(len(G))]
    for row in range(len(G)):
        for column in range(row+1,len(G)):
            if G[row][column] != 0:
                L_soms[row].append([column,G[row][column]])
                L_soms[column].append([row, G[row][column]])

    # Trzeba jeszczce pare tablic zrobić
    been_here = [False for _ in range(len(L_soms))]
    distances = [float('inf') for _ in range(len(L_soms))]

    # Trzeba by zrobić jakąś funkcje req
    # flaga: 1-poprzedni ruch to były 2mil buty, 0-poprzedni to nie były 2mil buty
    def req(curr_vertex,L_soms,curr_dystans,flaga,been_here):


        # Trzeba zaznaczyć dystans i been_here
        been_here[curr_vertex] = True
        if curr_dystans < distances[curr_vertex]:
            distances[curr_vertex] = curr_dystans

        # Teraz trzeba przejść do somsiadów, wpierw normalnie
        for somsiad in L_soms[curr_vertex]:
            if been_here[somsiad[0]] == False:
                req(somsiad[0],L_soms,curr_dystans+somsiad[1],0 ,been_here)

        # Teraz robimy milowe buty
        if flaga == 0:
            print('korzystam')
            for somsiad_1 in L_soms[curr_vertex]:
                for somsiad_2 in L_soms[somsiad_1[0]]:
                    print(f'z {curr_dystans} przez {somsiad_1[0]} do {somsiad_2[0]}')
                    if been_here[somsiad_2[0]] == False:
                        print('nie zajęte')
                        req(somsiad_2[0],L_soms,curr_dystans + max(somsiad_1[1],somsiad_2[1]),1,been_here)

        been_here[curr_vertex] = False
    # Trza jeszcze srobić seeda rekurzji
    req(s,L_soms,0,0,been_here)

    return distances[w]

print(jumper(G,0,0))

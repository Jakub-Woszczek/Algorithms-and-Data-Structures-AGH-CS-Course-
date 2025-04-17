# Aparrently juz to zrobiłem xddd

# ALe spróbóje dynamiqa

def jumper( G, s, w ):
    from queue import PriorityQueue

    # Tworze tablice somsiedztwa
    L_soms = [[] for _ in range(len(G))]
    for row in range(len(G)):
        for column in range(row + 1, len(G)):
            if G[row][column] != 0:
                L_soms[row].append([column, G[row][column]])
                L_soms[column].append([row, G[row][column]])

    # Trzeba jeszczce pare tablic zrobić
    been_here = [False for _ in range(len(L_soms))]
    n = len(G)

    DQ_possible = [float('inf') for _ in range(n)]
    DQ_impossible = [float('inf') for _ in range(n)]
    DQ_possible[s] = 0
    Q = PriorityQueue()

    queue_val = 1
    Q.put([0, s])  # Robie seeda BFS

    while not Q.empty():
        curr_v = Q.get()[1]
        been_here[curr_v] = True

        for somsiad_1, soms_weight_1 in L_soms[curr_v]:
            if been_here[somsiad_1] == False:
                # Tutaj rozpatruje normalny krok
                DQ_possible[somsiad_1] = min(soms_weight_1 + min(DQ_possible[curr_v], DQ_impossible[curr_v]),
                                             DQ_possible[somsiad_1])
                Q.put([queue_val, somsiad_1])

            for somsiad_2, soms_weight_2 in L_soms[somsiad_1]:
                if been_here[somsiad_2] == False:
                    # Tutaj rozpatruje dwumilowy krok
                    DQ_impossible[somsiad_2] = min(DQ_impossible[somsiad_2],
                                                   max(soms_weight_1, soms_weight_2) + DQ_possible[curr_v])

        queue_val += 1

    return min(DQ_possible[w], DQ_impossible[w])

S=[[0, 1, 0, 0], [1, 0, 2, 0], [0, 2, 0, 3], [0, 0, 3, 0]]
print(jumper(S,0,3))
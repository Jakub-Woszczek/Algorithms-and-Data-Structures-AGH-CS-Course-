def magic(C):

    n = len(C)
    DQ = [0 for _ in range(n)] # max ile sztabek może mieć będąc w i-tej komnacie
    avilable_to_roam = [False for _ in range(n)]
    avilable_to_roam[0] = True
    current_chamber = 0
    carried_gold = 0

    for data in C:
        if avilable_to_roam[current_chamber] == True:
            treasure = data[0]
            carried_gold = DQ[current_chamber]
            all_gold_avilable = treasure + carried_gold

            for i in range(1, 4):
                price, next_chamber = data[i]

                if next_chamber != -1:
                    if treasure > price + 10:
                        continue
                    else:

                        if treasure < price:
                            if all_gold_avilable >= price:
                                DQ[next_chamber] = max(DQ[next_chamber], all_gold_avilable - price)
                                avilable_to_roam[next_chamber] = True

                        else:
                            add = treasure - price
                            DQ[next_chamber] = max(carried_gold + add, DQ[next_chamber])
                            avilable_to_roam[next_chamber] = True

        current_chamber += 1


    return DQ[n-1] if avilable_to_roam[n-1] == True else -1

C = [ [8, [ 6, 3], [ 4, 2], [7, 1]], # 0
[22, [12, 2], [21, 3], [0,-1]], # 1
[9, [11, 3], [ 0,-1], [7,-1]], # 2
[15, [ 0,-1], [ 1,-1], [0,-1]] ] # 3

C_2 = [[2, [5, 1], [1, 6], [1, 8]],
[2, [7, 2], [1, 4], [1, 2]],
[89, [91, 3], [75, 8], [84, 6]],
[8, [6, 4], [10, 6], [7, 5]],
[4, [5, 5], [1, 7], [3, 5]],
[10, [11, 6], [0, 6], [4, 6]],
[1, [0, 7], [0, 7], [6, 7]],
[57, [51, 8], [45, 8], [50, 8]],
[2, [6, 9], [7, 9], [0, 9]],
[6, [3, -1], [8, -1], [1, -1]]]
# Ma być 11

print(magic(C_2))
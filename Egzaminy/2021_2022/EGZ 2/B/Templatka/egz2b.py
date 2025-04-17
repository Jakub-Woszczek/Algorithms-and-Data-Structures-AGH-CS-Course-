from egz2btesty import runtests

def magic( C ):
    n = len(C)
    DQ = [0 for _ in range(n)]  # max ile sztabek może mieć będąc w i-tej komnacie
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

    return DQ[n - 1] if avilable_to_roam[n-1] == True else -1
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )

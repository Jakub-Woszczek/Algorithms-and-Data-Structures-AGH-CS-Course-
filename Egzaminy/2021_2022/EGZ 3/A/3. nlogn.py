def snow(T,I):

    n = len(I)
    add_layer = []
    subs_layer = []
    for  start,end in I:
        add_layer.append(start)
        subs_layer.append(end)

    add_layer.sort()
    subs_layer.sort()




    add_sprh,subs_sprh = 0,0
    thnickness = 0
    max_thc = 0
    while add_sprh < n and subs_sprh < n:

        if add_layer[add_sprh] <= subs_layer[subs_sprh]:
            thnickness += 1
            add_sprh += 1

        else:
            thnickness -= 1
            subs_sprh += 1

        max_thc = max(max_thc,thnickness)


    return max_thc





T = 100
I = [[3,10],[0,5],[20,30],[25,35],[26,26]]
print(snow(T,I))
def snow(T,I):

    layers = [0]*T

    for start,end in I:
        layers[start] += 1
        layers[end+1] -= 1

    max_snow = 0
    snow_lvl = 0
    for i in range(T):
        snow_lvl += layers[i]
        max_snow = max(max_snow,snow_lvl)

    return max_snow

T = 100
I = [[3,10],[0,5],[20,30],[25,35],[26,26]]
print(snow(T,I))
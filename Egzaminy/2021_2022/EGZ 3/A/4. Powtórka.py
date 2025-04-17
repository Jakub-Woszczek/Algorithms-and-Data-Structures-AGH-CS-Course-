def snow(T,I):
    sorted_begining = []
    sorted_end = []

    I.sort(key=lambda x: x[0])
    for x,y in I:
        sorted_begining.append(x)

    I.sort(key=lambda x: x[1])
    for x,y in I:
        sorted_end.append(y)

    n = len(I)
    layer,max_layer = 0,0
    begining, end = 0, 0

    while begining < n:

        if sorted_begining[begining] <= sorted_end[end]:
            begining += 1
            layer += 1
            max_layer = max(max_layer,layer)
        else:
            end += 1
            layer -= 1
            max_layer = max(max_layer, layer)

    return max_layer
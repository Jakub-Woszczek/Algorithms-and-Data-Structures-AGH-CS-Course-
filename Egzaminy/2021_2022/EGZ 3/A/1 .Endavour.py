def snow(T,I):

    layers = [0]*T
    n = len(I)

    I.sort(key = lambda x : x[0])
    print(I)
    max_layer = 0
    path = [0 for _ in range(T)]
    layer = 0
    for i in range(T):


        if i == I[layer][0]:
            path[i] = path[i-1] + 1
            layer += 1
            if layer >= n:
                while i < T-1:
                    i += 1
                    path[i] = path[i - 1]
                break

        else:
            path[i] = path[i-1]

    print(path)

    I.sort(key = lambda x : x[1])
    layer = 0

    for m in range(T):
        print(path)
        print(path[m])
        if m-1 == I[layer][1]:
            path[m] = path[m-1] - 1
            layer += 1
            if layer >= n:
                break

        else:
            path[m] = path[m-1]

    print(path)
    return path

T = 100
I = [[3,10],[0,5],[20,30],[25,35],[26,26]]
snow(T,I)
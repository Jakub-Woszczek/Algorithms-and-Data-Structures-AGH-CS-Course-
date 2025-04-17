def print_2d_array(array):
    # Określ maksymalną szerokość liczby, aby wyrównać kolumny
    max_width = max(len(str(item)) for row in array for item in row)

    for row in array:
        print(" ".join(f"{item:>{max_width}}" for item in row))


def parking( X, Y ):

    parkingi = len(Y)
    biurowce = len(X)

    DQ = [[0 for _ in range(parkingi)] for _ in range(biurowce)]
    DQ[0][0] = abs(Y[0] - X[0])

    for i in range(1,parkingi):
        DQ[0][i] = min(DQ[0][i-1],abs(Y[i] - X[0]))

    for i in range(1,biurowce):
        DQ[i][i] = DQ[i-1][i-1] + abs(Y[i] - X[i])

    for biurowiec in range(1,biurowce):
        for paring in range(biurowiec+1,parkingi):

            DQ[biurowiec][paring] = min(DQ[biurowiec][paring-1],
                                      DQ[biurowiec-1][paring-1] + abs(Y[paring] - X[biurowiec]))

    print_2d_array(DQ)

    return DQ[biurowce-1][parkingi-1]


X = [3,6,10,14]
Y = [1,4,5,10,11,13,17]

print(parking(X,Y))
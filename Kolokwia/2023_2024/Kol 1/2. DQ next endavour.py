def maxrank(T):

    n = len(T)
    T_sorted = []

    i = 0
    for num in T:
        T.append([num,i])
        i += 1

    T_sorted.sort(key= lambda  x : x[0])

    

    return

T = [5,3,9,4]
print(maxrank(T))
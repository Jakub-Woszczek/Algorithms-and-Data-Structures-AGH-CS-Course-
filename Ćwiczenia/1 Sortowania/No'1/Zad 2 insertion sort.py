import random

def insertion_sort(T):
    n = len(T)

    for i in range(n):
        j = i
        cur_min = i
        while j < n:
            if T[cur_min] > T[j]:
                cur_min = j
            j+=1
        T[i],T[cur_min] = T[cur_min],T[i]
    return T

print(insertion_sort([random.randint(1,1000) for _ in range(10000)]))




def insert_sort(T):
    n = len(T)
    for i in range(1,n):
        j = i
        while j>0 and T[j-1] > T[j]:
            T[j-1],T[j] = T[j],T[j-1]
            j -=1
    return T

# print(insert_sort([5,4,2,3,1]))

def moj_insertion(T):
    n = len(T)

    for j in range(1,n):
        i = j
        while i>0 and T[i-1]>T[i]:
            T[i - 1],T[i] = T[i],T[i-1]
            i-=1

    return T

print(moj_insertion([5,4,3,2,1]))
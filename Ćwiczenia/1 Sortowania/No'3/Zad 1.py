# Quick sort z jak najmniejszą pamięcią
#Req z 1 wywołaniem
# Do przeanailzowania
def partition(A,p,r):
    pivot = A[p]
    lagt = 1+p
    for i in range(p+1,r):
        if A[i] < pivot:
            temp = A[i]
            A[i] = A[lagt]
            A[lagt] = temp
            lagt +=1
        A[0] = A[lagt-1]
        A[lagt-1]=pivot
        return lagt-1


def quicq_sort(A,p,r):
    while p < r:
        q = partition(A,p,r)
        if q - p < r-q:
            quicq_sort(A,p,q-1)
            p = q + 1
        else:
            quicq_sort(A,q+1,r)
            r = q -1

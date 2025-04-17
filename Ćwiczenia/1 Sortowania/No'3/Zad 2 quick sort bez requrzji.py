def quicqsort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicqsort(A,p,q-1)
        quicqsort(A, q+1,r)

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


def quick_sort_2(A):
    heap =[]
    heap.append((0,len(A)-1))
    while len(heap) != 0:
        temp = heap.pop()
        p = temp[0]
        r = temp[1]
    q = partition(A,p,r)
    heap.append((q+1,r))
    heap.append((p,q-1))
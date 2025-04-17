def buildHeap(A):
    n = len(A)
    for i in range(n//2-1,-1,-1):
        heapify(A,n,i)


def heapify(A,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and A[i] < A[left]:
        largest = left

    if right < n and A[largest] < A[right]:
        largest = right

    if largest != i:
        A[i],A[largest] = A[largest],A[i]

        heapify(A, n, largest)

def HeapSort(A):
    n = len(A)
    buildHeap(A)

    for i in range(n-1,0,-1):
        A[i], A[0] = A[0], A[i]
        heapify(A,i,0)
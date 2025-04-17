def ksum(T,k,p):
    n = len(T)
    sorted_T = quicksort(T[:p])
    for i in range(n-p+1):


def BoubbleSort(T):
    n = len(T)
    for i in range(n):
        for j in range(0,n-i-1):
            if T[j] > T[j+1]:
                T[j],T[j+1] = T[j+1],T[j]

    return T

def partition(T):
    x = -1
    n = len(T)
    mid = n // 2
    # Tutaj zrobiłem żeby szukało pivota z 5 liczb, może to przyspieszy
    if len(T) > 20:
        lista_do_pivota = []
        lista_do_pivota.extend([T[0], T[mid - 1], T[mid], T[mid + 1], T[n - 1]])
        lista_do_pivota_sorted = BoubbleSort(lista_do_pivota)
        T[0] = lista_do_pivota_sorted[0]
        T[mid - 1] = lista_do_pivota_sorted[mid - 1]
        T[mid] = lista_do_pivota_sorted[mid]
        T[mid + 1] = lista_do_pivota_sorted[mid + 1]
        T[n - 1] = lista_do_pivota_sorted[n - 1]

    pivot = mid
    T[pivot], T[n - 1] = T[n - 1], T[pivot]
    pivot = n - 1
    j = pivot -1
    for i in range(n):
        if i == j:
            T[i],T[pivot] = T[pivot],T[i]
            return i
        if T[i] > T[pivot]:
            while T[j] > T[pivot]:
                j -= 1
                if i == j:
                    T[i], T[pivot] = T[pivot], T[i]
                    return i
            T[i], T[j] = T[j], T[i]


def QuickSort(T):
    n = len(T)

    T,pivot = partition(T)

    QuickSort(T[pivot:])
    QuickSort(T[:pivot])

# Od Phalisza

def quicksort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)
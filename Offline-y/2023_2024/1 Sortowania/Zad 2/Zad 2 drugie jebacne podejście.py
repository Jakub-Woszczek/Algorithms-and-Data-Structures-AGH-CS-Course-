

def ksum(T,k,p):
    def quicksort(A, left, right):

        if left < right:
            pivot = partition(A, left, right)
            quicksort(A, left, pivot - 1)
            quicksort(A, pivot + 1, right)

    def partition(A, left, right):
        pivot = A[right]
        i = left - 1
        for j in range(left, right):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]

        A[i + 1], A[right] = A[right], A[i + 1]
        return i + 1

    def search_indexu(T,val):
        left = 0
        right = len(T)-1

        while left <= right:
            mid = (left+right)//2
            if T[mid] == val:
                return mid
            elif T[mid] < val:
                left = mid +1
            else:
                right = mid -1

    def binary_search_insert(arr, value):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == value:
                return mid
            elif arr[mid] < value:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def insert_sorted(arr, value):
        index = binary_search_insert(arr, value)
        arr.insert(index, value)


    n = len(T)
    j = p - 1
    sorted_list = quicksort(T[:p])
    suma = 0
    for i in range(n-p+1):
        suma += sorted_list[k-1]
        el_do_del = T[i]
        index_del = search_indexu(T,el_do_del)
        T.pop(index_del)
        insert_sorted(T,T[i+p])
    suma += sorted_list[k-1]
    return suma


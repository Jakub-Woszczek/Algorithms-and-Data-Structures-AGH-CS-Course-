# Tablica A zawiera liczby naturalne

def counting_sort(A,k):
    n = len(A)
    B = [None]*n
    C = [0]*k

    for x in A:
        C[x] += 1

    for i in range(1,k):
        C[i] += C[i - 1]

    for i in range(n-1, -1, -1):
        B[C[A[i]]-1]= A[i]
        C[A[i]] -=1

    return B

A = [3,1,2,3,4,2,4,1]
k = 4
print(counting_sort(A,k+1))
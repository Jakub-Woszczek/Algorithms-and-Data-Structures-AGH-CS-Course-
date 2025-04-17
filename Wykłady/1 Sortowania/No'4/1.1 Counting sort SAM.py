def counting_sort(A,k):
    n = len(A)
    Sorted = [None]*n
    amnt_of_num = [0]*k

    for i in range(n):
        amnt_of_num[A[i]] += 1

    for i in range(1,k):
        amnt_of_num[i] += amnt_of_num[i-1]

    for i in range(n-1,-1,-1):
        Sorted[amnt_of_num[A[i]]-1] = A[i]
        amnt_of_num[A[i]] -=1

    return Sorted

A = [3,1,2,3,4,2,4,1]
k = 4
print(counting_sort(A,k+1))
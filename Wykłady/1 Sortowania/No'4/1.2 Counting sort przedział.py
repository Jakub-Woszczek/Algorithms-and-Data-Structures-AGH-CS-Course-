def cnt_sort_przedzial(A):
    a = A[0]
    b = A[0]
    for i in range(len(A)):
        if A[i] < a:
            a = A[i]
        if A[i] > b:
            b = A[i]

    def cnt_sort(A,a,b):
        k = b-a+1
        n = len(A)
        amnt_of_num = [0]*k
        Sorted = [None]*n

        for i in range(n):
            amnt_of_num[A[i]-a] += 1

        for i in range(1,k):
            amnt_of_num[i] += amnt_of_num[i-1]

        for i in range(n-1,-1,-1):
            Sorted[amnt_of_num[A[i]-a]-1] = A[i]
            amnt_of_num[A[i] - a] -=1


        return Sorted



    return cnt_sort(A,a,b)

import random
a=10
b=20
n=100
T = [random.randint(a,b) for _ in range(n)]

print(cnt_sort_przedzial(T))
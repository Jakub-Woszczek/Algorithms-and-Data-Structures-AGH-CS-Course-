def mergesort(A):

    if len(A) == 1:
        return A
    n = len(A)
    array_one = mergesort(A[:n//2])
    array_two = mergesort(A[n // 2:])

    return scal(array_one,array_two)

def scal(A,B):
    c = []
    a = len(A)
    b = len(B)
    while len(A)>0 and len(B)>0:
        if A[0]<B[0]:
            c.append(A[0])
            A = A[1:]
            a-=1
        else:
            c.append(B[0])
            B = B[1:]
            b-=1

    if b>0:
        while b>0:
            c.append(B[0])
            B = B[1:]
            b -= 1
    else:
        while a>0:
            c.append(A[0])
            A = A[1:]
            a -= 1

    return c

list = [1,4,5,3,2,6,4,7,8]
list_2 = mergesort(list)
print(list_2)


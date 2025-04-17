def partition(A,p,r):
    pivot = A[(par)//2]
    i = p-1
    j = r+1
    while True:
        i +=1
        while A[i] < pivot:
            i+=1

        j -=1
        while A[j] > pivot:
            j -=1

        if i < j:
            A[i],A[j] = A[j],A[i]
        else:
            return j
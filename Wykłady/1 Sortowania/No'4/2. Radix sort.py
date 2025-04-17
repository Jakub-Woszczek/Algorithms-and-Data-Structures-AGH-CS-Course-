def radix_sort(T):
     smallest = T[0]
     for i in range(1,len(T)-1):
         if T[i] > smallest:
             smallest = T[i]


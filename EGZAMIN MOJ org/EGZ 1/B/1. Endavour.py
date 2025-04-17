def kstrong(T,k):

    prev_start,prev_end = T[0],T[0]
    start,end = 0,1
    n = len(T)
    curr_sum = T[0]
    while start < n:
        print(prev_end,end)
        while T[prev_end] > 0 and T[end] > 0:

            curr_sum += T[end]
            prev_end = end
            end += 1
        print(prev_end, end)
        print('')
        print(prev_start,start)
        while T[prev_start] < 0 and T[start] < 0:

            curr_sum -= T[prev_start]
            prev_start = start
            start += 1
        print(prev_start, start)

T = [1,-2,7,5,10]
k = 2

kstrong(T,k)

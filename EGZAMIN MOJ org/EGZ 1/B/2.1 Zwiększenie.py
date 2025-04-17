def kstrong(T,k):

    # Spr czy lenTslice > k:
    start,end = 0,1
    n = len(T)
    curr_sum = T[0]

    if T[0] >= 0 and T[1] >= 0:

        while start < n:

            while end < n:
                while T[end] > 0:
                    curr_sum += T[end]
                    end += 1

                curr_sum += T[end]
                end += 1

                while end < n and not (T[end] < 0 and T[end - 1] > 0):
                    curr_sum += T[end]
                    prev_end = end
                    end += 1

                print(start, end)

            while not(T[start] > 0 and T[start-1] < 0):
                curr_sum -= T[start]
                start += 1
            print(start, end)


T = [1,1,1,-2,-2,7,5,10,-1,-1,1,1]
k = 2

kstrong(T,k)
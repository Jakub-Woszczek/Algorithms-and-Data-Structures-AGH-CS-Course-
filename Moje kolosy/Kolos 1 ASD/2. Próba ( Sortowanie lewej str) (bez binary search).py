def maxrak(T):
    def merge_sort(T):

        def div(T):
            n = len(T)
            if n == 1:
                return T

            T_1 = T[:n // 2]
            T_2 = T[n // 2:]

            T_1 = merge_sort(T_1)
            T_2 = merge_sort(T_2)

            return merge(T_1, T_2)

        def merge(T1, T2):
            merged = []
            n1, n2 = len(T1), len(T2)

            while n1 > 0 and n2 > 0:
                if T1[0] < T2[0]:
                    merged.append(T1[0])
                    del T1[0]
                    n1 -= 1
                else:
                    merged.append(T2[0])
                    del T2[0]
                    n2 -= 1

            while n1 > 0:
                merged.append(T1[0])
                del T1[0]
                n1 -= 1

            while n2 > 0:
                merged.append(T2[0])
                del T2[0]
                n2 -= 1

            return merged

        return div(T)


    n = len(T)
    T_lewa = T
    # Tu trzeba posortować lewą stronę
    merge_sort(T_lewa)
    len_lewa = n-1
    max_cnt = 0
    for i in range(n-1,0,-1):
        if i <= max_cnt:
            return max_cnt

        # Tu poprostu szukam odpowiedzniej liczby do wykasowania
        key = T[i]
        index = 0
        while key > T_lewa[index]:
            index +=1
        del T_lewa[index]
        len_lewa -= 1
        if index > max_cnt:
            max_cnt = index


        # cnt = 0
        # while len_lewa > cnt and T_lewa[cnt] < key:
        #     cnt +=1
        #
        # if cnt > max_cnt:
        #     max_cnt = cnt
        # # del T_lewa[cnt]
        # len_lewa -=1

    return max_cnt


T = [5,3,9,4]
print(maxrak(T))
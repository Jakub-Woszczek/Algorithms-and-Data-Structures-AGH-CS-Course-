def maxrak(T):
    n = len(T)
    ranks_all = [0]*n
    max_cnt = 0
    for i in range(n-1,0,-1):
        cnt = 0
        if i <= max_cnt:
            return max_cnt
        for j in range(i-1,-1,-1):
            if T[j] < T[i]:
                cnt +=1
        ranks_all[i] = cnt
        if cnt > max_cnt:
            max_cnt = cnt

    return max_cnt

print(maxrak([5,3,9,4,8,1]))

def LIS_requrzjon(T):


    def lis_ending_at(i):

        if i == 0:
            return 1

        max_lenght = 1

        for j in range(i):
            if T[j] <= T[i]:
                max_lenght = max(max_lenght,lis_ending_at(j) + 1)

        return max_lenght

    # Będe liczył maxy dla każdej iteratki i wyciągle overallmax
    overall_max = 1

    for i in range(len(T)):
        overall_max = max(overall_max,lis_ending_at(i))

    return overall_max

def LIS_dynamiq(T):

    def lis_ending_at(i):

        if memeo[i] != 1:
            return memeo[i]

        max_lengt = 1

        for j in range(i):
            # print(T[j],T[i])
            if T[j] <= T[i]:
                max_lengt = max(max_lengt,lis_ending_at(j) + 1)

        # print(memeo,i)
        memeo[i] = max_lengt
        return max_lengt

    # Zrobie tablice Memorializacji
    memeo = [1 for _ in range(len(T))]

    oveall_max = 1

    for i in range(len(T)):
        oveall_max = max(oveall_max,lis_ending_at(i))

    return oveall_max

def LIS_dynamiq_phalisza(T):

    n = len(T)
    memo = [1]*n

    for first in range(1,n):
        for spr in range(first):
            if T[spr] <= T[first] and memo[first] < memo[spr]+1:
                memo[first] = memo[spr] + 1

    return max(memo)

def LIS_dynamiq_phalisza_mod(T):

    n = len(T)
    memo = [1]*n
    max_curr_memo = 1
    parent = [-1 for _ in range(n)]

    for first in range(1,n):
        for spr in range(first-1,-1,-1):
            if T[spr] <= T[first] and memo[first] < memo[spr]+1:
                memo[first] = memo[spr] + 1
                parent[first] = spr
                if max_curr_memo == memo[spr]:
                    max_curr_memo += 1
                    break
                max_curr_memo = max(max_curr_memo,memo[first])

    return max(memo),parent


def print_sol(Arr,parent,index):

    if parent[index] != -1:
        print_sol(Arr,parent,parent[index])

    print(arr[index], end=' ')






arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(LIS_requrzjon(arr))
print(LIS_dynamiq(arr))
print(LIS_dynamiq_phalisza(arr))
m,T = LIS_dynamiq_phalisza_mod(arr)

print_sol(arr,T,8)
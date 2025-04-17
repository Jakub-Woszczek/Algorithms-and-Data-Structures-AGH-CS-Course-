def wired(T):

    n = len(T)
    memo = [[None for _ in range(n+1)] for _ in range(n+1)]

    # F req
    def min_cost(i,j):
        nonlocal memo

        if memo[i][j] != None:
            return memo[i][j]

        if i >= j:
            return 0

        if i+1 == j:
            return 1 + abs(T[i] - T[j])

        min_cost_val = float('inf')

        for k in range(i + 1,j + 1,2):

            cost = 1 + abs(T[i] - T[k])
            total_cost = cost + min_cost(i + 1,k - 1) + min_cost(k+1,j)

            min_cost_val = min(min_cost_val,total_cost)

        memo[i][j] = min_cost_val


        return min_cost_val


    return min_cost(0, n - 1)

T2 = [39, 90, 72, 7, 65, 80, 30, 82, 19, 73, 94, 18, 29, 1] # 140 -> 133 bez n/2
print(wired(T2))
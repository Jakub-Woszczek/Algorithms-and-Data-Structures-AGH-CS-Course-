def monety(nom,k):

    dp = [float('inf') for _ in range(xd )]

    dp[0] = 0

    for i in range(1,k-1):
        for x in nom:
            if i-x >= 0:
                dp[i] = min(dp[i],dp[i-x] + 1)

    return dp[k]
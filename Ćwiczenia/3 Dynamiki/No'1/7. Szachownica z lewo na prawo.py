def bruhhhhhhh(P):
    dp = []

    dp[i][j] = min(dp[i-1][j],dp[i][j-1] + P[i][j])
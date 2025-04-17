from zad6ktesty import runtests 

def haslo ( S ):
    if '00' in S:
        return 0

    n = len(S)

    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    if S[1] != '0':
        dp[1] = 1

    for i in range(2, n + 1):

        cyfra = int(S[i - 1:i])
        if cyfra != 0:
            dp[i] += dp[i - 1]

        liczpa = int(S[i - 2:i])
        if 10 <= liczpa <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

    return -1

runtests ( haslo )
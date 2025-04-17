from zad3ktesty import runtests

def ksuma( T, k ):
    n = len(T)
    dp = [float('inf')] * (n + 1)  # Tablica dp z wartościami nieskończoności
    dp[0] = 0  # Dla zerowego elementu, minimalna suma to 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + T[i - j])

    # Wynikiem jest dp[n], czyli minimalna k-ładna suma dla całej tablicy
    return dp[n]
    return 0
    
runtests ( ksuma )
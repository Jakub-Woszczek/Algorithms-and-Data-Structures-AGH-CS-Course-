def palindrom( S ):

    n = len(S)

    def odd_number(S, mid):
        n = len(S)

        left = mid - 1
        right = mid + 1
        while left > -1 and right < n and S[left] == S[right]:
            left -= 1
            right += 1

        return (right - mid - 1) * 2 + 1

    def even_nums(S, left, right):

        n = len(S)

        while left > -1 and right < n and S[right] == S[left]:
            print(S[right], S[left])
            left -= 1
            right += 1

        return right - left - 1 if (left > -1 and right < n) else right - left - 1

    max_pali = 0
    for i in range(1,n-2):
        max_pali = max(max_pali,odd_number(S,i))

    for left in range(1,n-3):
        right = left + 1

        max_pali = max(max_pali,even_nums(S,left,right))

    return max_pali

print(palindrom('sdrgsasdfdsa'))
def palindrom( S ):

    n = len(S)

    def odd_number(S, mid):
        n = len(S)

        left = mid - 1
        right = mid + 1
        while left > -1 and right < n and S[left] == S[right]:
            left -= 1
            right += 1
        lenght = (right - mid - 1) * 2 + 1
        return lenght,[left+1,right-1]

    def even_nums(S, left, right):

        n = len(S)

        while left > -1 and right < n and S[right] == S[left]:
            print(S[right], S[left])
            left -= 1
            right += 1

        return right - left - 1,[left+1,right-1]

    max_pali = 0
    for i in range(1,n-2):
        lenght,coordinates = odd_number(S,i)
        if lenght > max_pali:
            max_pali,cords = lenght,coordinates



    for left in range(1,n-3):
        right = left + 1

        lenght, coordinates = even_nums(S, left,right)
        if lenght > max_pali:
            max_pali, cords = lenght, coordinates

    x,y = cords
    return S[x:y+1]

print(palindrom('rkhgbasdfdsaaskjgfh'))
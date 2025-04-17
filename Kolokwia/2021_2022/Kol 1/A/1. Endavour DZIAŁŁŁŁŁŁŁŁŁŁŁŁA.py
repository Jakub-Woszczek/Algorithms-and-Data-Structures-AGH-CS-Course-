def g(T):
    def reverse_if_needed(s):
        # Sprawdzamy tylko, czy długość jest większa niż 1, aby nie sprawdzać pustych lub jednoliterowych stringów
        if len(s) <= 1:
            return s

        i = 0
        j = len(s) - 1

        # Przechodzimy przez string od początku i końca
        while i < j:
            if s[i] > s[j]:  # Pierwsza litera jest dalej w alfabecie
                return s[::-1]  # Odwracamy string
            elif s[i] < s[j]:  # Pierwsza litera jest wcześniej w alfabecie
                return s  # Nie odwracamy
            # Jeśli są takie same, idziemy dalej
            i += 1
            j -= 1

        return s

    n = len(T)

    for i in range(len(T)):
        T[i] = reverse_if_needed(T[i])

    T.sort()
    print(T)


    max_strike = 0
    strike = 1
    el_of_strike = T[0]
    for i in range(1,n):
        if T[i] == el_of_strike:
            strike += 1

        else:
            el_of_strike = T[i]
            max_strike = max(max_strike,strike)
            strike = 1

    return max_strike

T1 = ['pies', 'mysz', 'kot', 'kogut', 'tok', 'seip', 'kot']
print(g(T1))
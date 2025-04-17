def tower(A):
    n = len(A)
    lista = []
    for x,y in A:
        lista.append([x,y,0])

    def check(i1,i2):
        x1,y1,b = lista[i1]
        x2,y2,b = lista[i2]
        if x1 <= x2 and y1 <= y2:
            return True
        return False


    def req(org,index):
        print(f'jestem w {index}')
        suma = 0
        if index >= n-1:
            if check(org,index) == True:
                print(f'jestem w index {index} i zaliczam org {org}')
                return 1
            return 0


        if check(org,index) == True:
            print(f'jestem w index {index} i zaliczam do org {org}')
            suma = 1 + req(org,index + 1)

        else:
            suma = req(org,index + 1)

        return suma

    suma_max = 0
    for i in range(n-1):
        suma_max = max(suma_max,1 + req(i,i+1))

    print(suma_max)
    return suma_max

A = [(1,4),(0,5),(1,5),(2,6),(2,4)]
A_2 = [(1, 4), (0, 6), (1, 5), (2, 4), (2, 4), (2, 3)]
# tower(A_2)



# GPT

def tower_2(A):
    n = len(A)

    # Sortujemy klocki po pierwszym elemencie rosnąco, a jeśli te są równe, po drugim malejąco.
    A.sort(key=lambda x: (x[0], -x[1]))

    # Tablica do przechowywania wyników (memoizacja)
    memo = [-1] * n

    # Funkcja rekurencyjna do znajdowania maksymalnej wysokości wieży, zaczynając od klocka `i`
    def rec(i):
        # Jeśli wynik dla `i` został już policzony, zwróć go
        if memo[i] != -1:
            return memo[i]

        max_height = 1  # Zawsze możemy użyć przynajmniej jeden klocek (sam `i`)

        # Sprawdź wszystkie wcześniejsze klocki
        for j in range(i):
            if A[j][0] <= A[i][0] and A[j][1] >= A[i][1]:  # Jeśli klocek j może być pod klockiem i
                max_height = max(max_height, 1 + rec(j))

        # Zapisz wynik dla `i` w tablicy memo
        memo[i] = max_height
        return max_height

    # Znajdź maksymalną wysokość wieży, biorąc pod uwagę każdy klocek jako potencjalny ostatni klocek
    max_tower = 0
    for i in range(n):
        max_tower = max(max_tower, rec(i))

    return max_tower


# Przykładowe dane testowe
# A = [(1, 4), (0, 5), (1, 5), (2, 6), (2, 4)]
# A_2 = [(10, 15), (8, 14), (1, 6), (3, 10), (8, 11), (6, 15)]

# Testowanie funkcji
# print(tower(A))  # Oczekiwany wynik: 3
print(tower_2(A_2))  # Oczekiwany wynik: 2

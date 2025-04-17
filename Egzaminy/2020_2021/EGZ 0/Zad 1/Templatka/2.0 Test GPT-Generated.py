import random
import string


def tanagram(x, y, t):
    def czy_posortowana(tablica):
        return tablica == sorted(tablica)
    def indeksy_wystapien(slowo):
        T = [[None] for _ in range(26)]
        odwiedzone = []

        i = 0
        for litera in slowo:
            index = ord(litera) - 97
            T[index].append(i)
            i += 1

        return T

    T = indeksy_wystapien(x)

    def mirror_indexes(org,new_word):
        T_new = []
        for letter in new_word:
            index = ord(letter)-97

            i = 0
            while org[index][i] == None and i < len(org[index])-1:
                i += 1
            T_new.append(org[index][i])
            org[index][i] = None

        return T_new

    T_vol2 = mirror_indexes(T,y)

    def buble_sort(napis,iteracje):

        for _ in range(iteracje):
            for  i in range(len(napis)-1):

                if napis[i] > napis[i+1]:
                    napis[i],napis[i+1] = napis[i+1],napis[i]

        return napis

    k_sortow = buble_sort(T_vol2,t)

    return czy_posortowana(k_sortow)
    pass


def is_tanagram_naive(x, y, t):
    n = len(x)
    if len(y) != n:
        return False

    for i in range(n):
        found_match = False
        for j in range(max(0, i - t), min(n, i + t + 1)):
            if x[i] == y[j]:
                found_match = True
                break
        if not found_match:
            return False

    return True


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def run_random_tests(num_tests=100, max_length=1000):
    passed = 0

    for i in range(num_tests):
        length = random.randint(1, max_length)
        t = random.randint(0, length - 1)

        # Generujemy dwa losowe napisy
        x = generate_random_string(length)
        y = list(x)

        # Przestawiamy losowo litery w y
        random.shuffle(y)
        y = ''.join(y)

        # Sprawdzamy za pomocą funkcji naiwnej
        expected = is_tanagram_naive(x, y, t)

        # Sprawdzamy za pomocą funkcji tanagram
        result = tanagram(x, y, t)

        if result == expected:
            print(f"Test {i + 1} PASSED")
            passed += 1
        else:
            print(f"Test {i + 1} FAILED: expected {expected}, got {result}")
            print(f"x: {x}")
            print(f"y: {y}")
            print(f"t: {t}")

    print(f"\nLiczba zaliczonych testów: {passed}/{num_tests}")


if __name__ == "__main__":
    run_random_tests()

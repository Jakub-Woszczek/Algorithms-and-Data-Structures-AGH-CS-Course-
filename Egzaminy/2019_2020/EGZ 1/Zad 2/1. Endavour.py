def opt_sum(T):
    T = sorted(T)

    n = len(T)
    curr_sum = 0
    max_dif = 0

    prawo = n-1
    lewo = 0
    if T[prawo] > abs(T[lewo]):
        curr_sum += T[prawo]
        prawo -= 1
    else:
        curr_sum += T[lewo]
        lewo += 1

    while lewo <= prawo:

        if curr_sum > 0:
            curr_sum += T[lewo]
            lewo += 1

        elif curr_sum < 0:
            curr_sum += T[prawo]
            prawo -= 1

        else:
            if abs(T[lewo]) > T[prawo]:
                curr_sum += T[prawo]
                prawo -= 1

            else:
                curr_sum += T[lewo]
                lewo += 1

        max_dif = max(max_dif,abs(curr_sum))

    return max_dif

T = [2,3,4]
print(opt_sum(T))


def test_opt_sum():
    # Test 1: Prosty przypadek
    assert opt_sum([1, -5, 2]) == 3, "Test 1 failed"

    # Test 2: Same dodatnie liczby
    assert opt_sum([2, 3, 4]) == 9, "Test 2 failed"

    # Test 3: Same ujemne liczby
    assert opt_sum([-2, -3, -4]) == 9, "Test 3 failed"

    # Test 4: Przypadek mieszany
    assert opt_sum([10, -3, 5, -7]) == 5, "Test 4 failed"

    # Test 5: Zera w tablicy
    assert opt_sum([0, -5, 0, 5]) == 5, "Test 5 failed"

    # Test 6: Jedna duża liczba dodatnia, jedna mała liczba ujemna
    assert opt_sum([100, -1]) == 99, "Test 6 failed"

    print("All tests passed!")

test_opt_sum()
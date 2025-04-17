import numpy


def anag(A, B):
    tab_A = [0]*26
    tab_B = [0]*26
    n = len(A)
    for i in range(n):
        tab_A[A[i] - 'A'] += 1
        tab_B[A[i]-'A'] -= 1

    for i in range(26):
        if tab_A[i] != 0: return False
    return True


def anag_V2(A, B,k):
    tab_A = numpy.empty(k)
    n = len(A)

    for i in range(n):
        tab_A[A[i] - 'A'] = 0
        tab_A[A[i] - 'A'] = 0

    tab_A = [0] * 26
    tab_B = [0] * 26
    for i in range(n):
        tab_A[A[i] - 'A'] += 1
        tab_B[A[i] - 'A'] -= 1

    for i in range(26):
        if tab_A[i] != 0: return False
    return True



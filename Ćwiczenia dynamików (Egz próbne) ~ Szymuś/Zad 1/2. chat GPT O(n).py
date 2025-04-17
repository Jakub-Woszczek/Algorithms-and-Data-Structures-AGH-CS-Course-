def roznica(S):
    # Zamień '0' na +1 i '1' na -1
    przeksztalcony_ciag = [1 if c == '0' else -1 for c in S]

    # Algorytm Kadane'a do znalezienia maksymalnej sumy podciągu
    max_ending_here = max_so_far = przeksztalcony_ciag[0]
    print(przeksztalcony_ciag)
    for x in przeksztalcony_ciag[1:]:

        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        print(x,max_ending_here,max_so_far)

    przeksztalcony_ciag_v2 = [-1 if c == '0' else 1 for c in S]

    # Algorytm Kadane'a do znalezienia maksymalnej sumy podciągu
    max_ending_here_2 = max_so_far_2 = przeksztalcony_ciag_v2[0]
    print(przeksztalcony_ciag_v2)
    for x in przeksztalcony_ciag_v2[1:]:
        max_ending_here_2 = max(x, max_ending_here_2 + x)
        max_so_far_2 = max(max_so_far_2, max_ending_here_2)
        print(x, max_ending_here_2, max_so_far_2)

    # Jeśli maksymalna suma jest mniejsza niż 0, oznacza to, że ciąg zawiera tylko jedynki
    max_all = max(max_so_far,max_so_far_2)
    return max_all if max_all > 0 else -1


# Przykłady użycia:
print(roznica("1111110"))  # Wynik: 4

def ksuma( T, k ):

    def find_min_value_and_last_index(lst):
        if not lst:  # sprawdzenie czy lista nie jest pusta
            return None, None

        min_value = float('inf')
        max_index = -1

        for i, value in enumerate(lst):
            if value < min_value:
                min_value = value
                max_index = i
            elif value == min_value:
                max_index = i

        return min_value, max_index

    n = len(T)
    last_sum_index = 0
    suma_k_ladna = 0

    while last_sum_index < n-k:

        val,curr_index = find_min_value_and_last_index(T[last_sum_index:last_sum_index+k])
        suma_k_ladna += val
        last_sum_index = last_sum_index + curr_index + 1

    return suma_k_ladna

T = [1, 2, 3, 4, 6, 15, 8, 7]
print(ksuma(T,4))

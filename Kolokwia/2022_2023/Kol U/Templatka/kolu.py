from kolutesty import runtests

def ice_cream( T ):
    print(T)
    T_supreme = []
    n = len(T)
    suma = 0

    def dzielenie_tablicy_iteracyjnie(T):
        stack = [(T, 0)]  # Stos, który przechowuje pary: (tablica do przetworzenia, liczba do odjęcia)

        while stack:
            T_to_split, substract = stack.pop()
            n = len(T_to_split)
            T_bigger_than_N = []
            T_rest = []

            for el in T_to_split:
                if el - substract > n:
                    T_bigger_than_N.append(el - substract)
                elif el - substract > 0:
                    T_rest.append(el - substract)

            T_supreme.append(T_bigger_than_N)

            # Jeśli mamy elementy w T_rest, dodajemy nowy stan na stos
            if len(T_rest) > 0:
                stack.append((T_rest, len(T_bigger_than_N)))

    dzielenie_tablicy_iteracyjnie(T)

    for tablica in T_supreme:
        i = 0
        for el in tablica:
            suma += el - i
            i += 1

    return suma
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )

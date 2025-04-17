import random
import time


def chaos_index(T):
    n = len(T)
    T_sorted = sorted(T)  # Sortujemy tablicę, aby uzyskać T_sorted
    index_map = {value: [] for value in T_sorted}

    # Przypisujemy oryginalne indeksy każdej wartości w T_sorted
    for i, value in enumerate(T):
        index_map[value].append(i)

    max_k = 0

    # Iterujemy przez posortowaną tablicę i obliczamy maksymalne przesunięcie
    for i in range(n):
        original_indices = index_map[T_sorted[i]]
        # Pobieramy pierwszy wolny indeks z listy oryginalnych indeksów
        original_index = original_indices.pop(0)
        # Obliczamy przesunięcie
        k = abs(original_index - i)
        max_k = max(max_k, k)

    return max_k


# Przykładowa funkcja algorytmu użytkownika
def expected_algorithm(input_data):
    return chaos_index(input_data)


# Funkcja mojego algorytmu
def my_algorithm(T):
    def is_sorted(T):
        return sorted(T) == T

    n = len(T)
    max_strike = 0

    for k in range(n):
        if is_sorted(T) == True:
            return max(k, max_strike)
        strike = 0
        for i in range(n - 1):
            if T[i] > T[i + 1]:
                T[i], T[i + 1] = T[i + 1], T[i]
                strike += 1



            else:
                strike = 0

            max_strike = max(max_strike, strike)

    return max(k, max_strike)


# Funkcja generująca losowe testy
def generate_random_test():
    # Generuje losową listę liczb całkowitych
    size = random.randint(1, 10000)  # Rozmiar listy od 1 do 100 elementów
    test_data = [random.randint(-10000, 10000) for _ in range(size)]  # Elementy z zakresu -1000 do 1000
    return test_data


# Funkcja sprawdzająca poprawność wyników
def check_result(input_data):
    # Oczekiwany wynik
    expected_result = expected_algorithm(input_data)
    # Wynik mojego algorytmu
    my_result = my_algorithm(input_data)

    # Porównanie wyników
    if my_result == expected_result:
        return True
    else:
        print(f"Błąd dla danych: {input_data}")
        print(f"Oczekiwany wynik: {expected_result}")
        print(f"Wynik mojego algorytmu: {my_result}")
        return False


# Funkcja testująca
def test_algorithm(num_tests=1000):
    all_tests_passed = True
    total_time = 0.0  # Zmienna do przechowywania sumy czasów wszystkich testów

    for _ in range(num_tests):
        # Generowanie losowego testu
        test_data = generate_random_test()

        # Mierzenie czasu działania mojego algorytmu
        start_time = time.time()
        my_algorithm(test_data)
        end_time = time.time()

        # Dodanie czasu trwania tego testu do sumy
        total_time += (end_time - start_time)

        # Sprawdzenie wyniku
        if not check_result(test_data):
            all_tests_passed = False

    # Wyświetlenie sumarycznego czasu działania
    print(f"Sumaryczny czas działania: {total_time:.6f} sekund")

    if all_tests_passed:
        print("Wszystkie testy zakończyły się sukcesem!")
    else:
        print("Niektóre testy zakończyły się niepowodzeniem.")


# Uruchomienie testów
if __name__ == "__main__":
    test_algorithm(100)

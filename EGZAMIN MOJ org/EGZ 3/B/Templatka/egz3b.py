# Jakub Woszczek

# Mój algorytm opiera się na tym że licze długości kolejnych odcinków między pechowymi liczbami i wtedy otrzymuje tablice
# 'L_ciongi' która wygląda tak: [1,1,2,1,1,1,12] jeżeli chodzi o  podany w zadaniu przykład, mam też pomocniczą tablice
# 'L_czy_unlucky' która mi potwierdza czy dana liczba w L_ciongi to pechowa, czy nie pechowa ale jest otoczona pechowymi
# Następnie tworze tablice dynamiczną (tylko z nazwy) gdzie row->ilość pechowych w ciągu, col-> o ile podciągów dodałem

# Szacuje złożoność czasową na O(n)

from egz3btesty import runtests


def kunlucky(T, k):
  def T_pech_creator(T, k):
    # Ta funcja tworzy wszystkie wyrazy ciągu do pierwszego większego od max_num profesora
    # żeby w czasie O(n) sprawdzić która z liczb profesora jest pechowa
    prof_max_num = max(T)

    T_pechowa = [k]
    prev = k
    i = 2
    while prev < prof_max_num:
      num = prev + prev % (i-1) + 7
      T_pechowa.append(num)
      i += 1
      prev = num

    return T_pechowa, prev + 1

  T_pechowa, max_num = T_pech_creator(T, k) # Tutaj mam liczby pechowe
  T_all = [False for _ in range(max_num + 1)] # Tutaj mam tablice o długości max liczby profesora
  for el in T_pechowa: # Zapisuje która z liczb profesora jest pechowa
    T_all[el] = True


  def przygotowanie_do_DQ(T, L_ciongi, L_czy_unlucky, T_check):
    # Tutaj mam funkcje króra tworzy omawiane na początku podciągi

    strike = 0

    for num in T:

      if T_check[num] == True: # Trafiam na pechową liczbe
        if strike > 0: # Dodaje zakończony ciąg jeżeli isnieje

          L_ciongi.append(strike)
          L_czy_unlucky.append(False)

        # Dodaje pechową liczbe
        L_ciongi.append(1)
        L_czy_unlucky.append(True)
        strike = 0

      else: # Zwykła liczba czyli zwiększam długość podciągu
        strike += 1

    if strike > 0:
      # Jest opcja że się talblica profesora nie zakończy liczbą
      # pechową wtedy trzeba dodać ostatni podciąg
      L_ciongi.append(strike)
      L_czy_unlucky.append(False)

    return L_ciongi, L_czy_unlucky

  L_ciongi, L_czy_unlucky = przygotowanie_do_DQ(T, [], [], T_all)

  DQ = [[None for _ in range(len(L_ciongi))] for _ in range(3)]
  max_possible = 0 # Tutaj zapisuje maksymalny podciąg który wystąpił

  # Tutaj przygotowywuje DQ dla podciągu bez żadnej pechowej liczby
  for i in range(len(L_ciongi)):
    if L_czy_unlucky[i] == True:
      DQ[0][i] = 0

    else:
      DQ[0][i] = L_ciongi[i]


  for col in range(1, len(L_ciongi)):
    for row in range(1, 3):

      if L_czy_unlucky[col] == False: # Jeżeli jest to normalny podciąg to zwiększam poprzedni o niego
        if DQ[row][col - 1] != None:
          DQ[row][col] = DQ[row][col - 1] + L_ciongi[col]
          max_possible = max(max_possible, DQ[row][col])


      else: # Jeżeli jest to to pechowa liczba to zwiększając o 1 przechodze o rząd niżej
        if DQ[row - 1][col - 1] != None:
          DQ[row][col] = DQ[row - 1][col - 1] + L_ciongi[col]
          max_possible = max(max_possible, DQ[row][col])



  return max_possible
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )

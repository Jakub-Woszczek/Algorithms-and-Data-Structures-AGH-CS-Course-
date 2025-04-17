def print_tablica_2d(tablica):
    # Znajdź maksymalną szerokość elementu w tablicy dla wyrównania kolumn
    max_len = max(len(str(element)) for row in tablica for element in row)

    for row in tablica:
        for element in row:
            # Wyświetl każdy element z odpowiednim wyrównaniem
            print(f"{str(element).ljust(max_len)}", end=" ")
        print()  # Nowa linia po każdym wierszu

def roznica( S ):

    def czy_sama_jedynki(liczba_binarna):
        return all(znak == '1' for znak in liczba_binarna)

    if czy_sama_jedynki(S) == True:
        return -1

    # Ustawienie tabicy dynamicznej
    n = len(S)
    DQ = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        DQ[i][i] = [1,0] if S[i] == '0' else [0,1]

    max_diffrence = 0
    # Biedne n^2
    for i in range(n):
        for j in range(i+1,n):
            DQ[i][j] = [DQ[i][j-1][0] + 1,DQ[i][j-1][1]] if DQ[j][j][0] == 1 else [DQ[i][j-1][0],DQ[i][j-1][1] + 1]
            max_diffrence = max(max_diffrence,abs(DQ[i][j][0] - DQ[i][j][1]))

    return max_diffrence
    return DQ

test_nie_dziala = '10001011111001010101' # Odp = 5
binary  = '110100'
print(roznica(test_nie_dziala))
# T = roznica(binary)
# print_tablica_2d(T)

# print(roznica('110100'))

# Narazie spróbóje zaimplementować to że stowrze tabilce 2D do tego zdjęcia i z tablicy 2D na 1D

def z_1D_na_2D(T,rows,last_row_people):

    T_2D = [[None for _ in range(rows + last_row_people - 1)] for _ in range(rows)]

# Dostajemi tablice n liczb naturalnych i parametr t
# i algorytm który sumuje do wartości t podciąg
#


def subsq(T,A):

    F = [0]*len(T)

    for  i in range(T-1):
        for j in range(n):
            F[i][j] = F[W-A[i]][i-1] or F[W][i-1]


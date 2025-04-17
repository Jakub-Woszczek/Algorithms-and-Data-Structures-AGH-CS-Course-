# Jakub Woszczek
#Algorytm polega na tym że biorę po kolei każdy element z listy i liczę
# ile punktów dominuje i jeżeli trafi na pkt który go dominuje to jest
# przerywana pętla
#
# Złożoność tego algorytmu to O(n^2)


from zad3testy import runtests

def dominance(P):
  cnt_max = 0
  for i in range(len(P)):
    cnt = 0
    x, y = P[i]

    for i in range(0, i):
      if P[i][0] > x and P[i][1] > y:
        break
      if P[i][0] < x and P[i][1] < y:
        cnt += 1
    for i in range(i + 1, len(P)):
      if P[i][0] > x and P[i][1] > y:
        break
      if P[i][0] < x and P[i][1] < y:
        cnt += 1

    if cnt > cnt_max:
      cnt_max = cnt

  return cnt_max


  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

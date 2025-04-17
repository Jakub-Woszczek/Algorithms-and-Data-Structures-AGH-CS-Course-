# Jakub Woszczek

# Ta implementacja kodu działa tak że idzie iterator od Lewej strony do prawej
# i dla krzdej iteracji dla 'i' idzie j ( w lewo) które dla danego i sprawdza
# ile jest mniejszych liczb.
# Usprawnienie dodałem takie że  mam max_cnt który zbiera dotychczasowe max_ranki
# i jeżeli w pewnym momencie będzie on większy od i to zanczy że nie zjadzie się
# już żadne i które by miało większy max_rank

# Złożoność obliczeniowa to O(n^2) , natomiast myśle że jest to O(n^2 / 2) lecz
# to raczej podchodzi pod O(n^2)

from kol1testy import runtests

def maxrank(T):
  n = len(T)
  ranks_all = [0] * n
  max_cnt = 0
  for i in range(n - 1, 0, -1):
    cnt = 0
    if i <= max_cnt:
      return max_cnt
    for j in range(i - 1, -1, -1):
      if T[j] < T[i]:
        cnt += 1
    ranks_all[i] = cnt
    if cnt > max_cnt:
      max_cnt = cnt

  return max_cnt

  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )

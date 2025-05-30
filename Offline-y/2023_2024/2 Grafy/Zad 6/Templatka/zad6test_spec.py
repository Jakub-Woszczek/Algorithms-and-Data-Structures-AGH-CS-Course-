2# zad6test_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# test  G  s  w  hint
  (0, [ [[0,1],[1,0]],0,1 ],1),
  (1, [ [[0, 2, 0],[2, 0, 3],[0, 3, 0]],0,2 ],3),
  (3, [ [[0, 1, 0, 0],[1, 0, 2, 0],[0, 2, 0, 3],[0, 0, 3, 0]],0,3 ],4), 
  (4, [ [[0, 1, 3, 0],[1, 0, 1, 2],[3, 1, 0, 4],[0, 2, 4, 0]],0,3 ],2),
  (5, [ [[0, 10, 1, 0],[10, 0, 10, 0],[1, 10, 0, 2],[0, 0, 2, 0]],0,3],2),
  (6, [ [[0, 1, 3, 0],[1, 0, 1, 2],[3, 1, 0, 4],[0, 2, 4, 0]],3,0],2),
  (7, [ [[0,1,3,4,0],[1,0,0,2,0],[3,0,0,5,6],[4,2,5,0,3],[0,0,6,3,0]],0,4],4),
  (8, [ [[0,2,6,0,0],[2,0,3,0,0],[6,3,0,1,6],[0,0,1,0,1],[0,0,6,1,0]],0,4],5),
  (9, [ [[0, 1, 0, 0, 0, 0],[1, 0, 2, 2, 0, 0],[0, 2, 0, 0, 3, 0],[0, 2, 0, 0, 3, 0],[0, 0, 3, 3, 0, 1],[0, 0, 0, 0, 1, 0]],0,5],5),
  (10, [ [[0, 1, 200, 200, 200, 200],
          [1, 0, 2, 200, 200, 200],
          [200, 2, 0, 40, 200, 200],
          [200, 200, 40, 0, 40, 200],
          [200, 200, 200, 40, 0, 117],
          [200, 200, 200, 200, 117, 0]],0,5],159),
  (11, [ [[0, 1, 200, 200, 200, 200],
          [1, 0, 2, 200, 200, 200],
          [200, 2, 0, 40, 200, 200],
          [200, 200, 40, 0, 40, 200],
          [200, 200, 200, 40, 0, 117],
          [200, 200, 200, 200, 117, 0]],0,4],43),
  (12, [ [[0, 1, 200, 200, 200, 200],
          [1, 0, 2, 200, 200, 200],
          [200, 2, 0, 40, 200, 200],
          [200, 200, 40, 0, 40, 200],
          [200, 200, 200, 40, 0, 117],
          [200, 200, 200, 200, 117, 0]],1,5],159),
  (13, [ [[0,9,5,0,0],[9,0,0,1,0],[5,0,0,9,0],[0,1,9,0,10],[0,0,0,10,0]],0,4 ],15),

]



from testy import MY_random

def my_randint(a,b):
  return a+MY_random()%(b-a+1)

def gentest(test, arg, hint ):
  if test<14:
    return arg,hint
  
  # generowanie danych

  return [G,s,w],hint
   

  

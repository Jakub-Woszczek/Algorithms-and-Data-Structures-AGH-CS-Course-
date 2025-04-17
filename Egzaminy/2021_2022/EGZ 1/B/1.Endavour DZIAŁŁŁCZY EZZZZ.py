class Node:
    def __init__( self,name = "A"):
        self.left = None
        self.right = None
        self.x = None
        self.name = name

    def __repr__(self):
        return str(self.name)

def widentall( T ):
    levels = []

    def find_best_lvl(A,curr_lvl):

        if len(levels) < curr_lvl+1:
            levels.append(1)
        else:
            levels[curr_lvl] += 1

        if A.right != None:
            find_best_lvl(A.right,curr_lvl+1)

        if A.left != None:
            find_best_lvl(A.left,curr_lvl+1)

    find_best_lvl(T,0)
    all_to_cut = 0

    def cut_branches(A,max_lvl,curr_lvl):

        nonlocal all_to_cut

        if curr_lvl == max_lvl: # Dotarłem do dobrego poziomu
            if A.right != None:
                all_to_cut += 1
                print(f"{A} odciąłem prawy")
            if A.left != None:
                all_to_cut += 1
                print(f"{A} odciąłem lewy")

            A.x = True

            return # Coś by można zreturnować

        if A.right == None and A.left == None and curr_lvl < max_lvl:
            A.x = False
            print(f"{A} ustawiam na False (za krótka)")
            return


        if A.left != None:
            cut_branches(A.left,max_lvl,curr_lvl + 1)
        if A.right != None:
            cut_branches(A.right,max_lvl,curr_lvl + 1)

        if A.right != None and A.right.x == False and A.left != None and A.left.x == False:
            A.x = False
            print(f"{A} obydwa dzieci to false")

        if A.right != None and A.right.x == True and A.left != None and A.left.x == True:
            A.x = True
            print(f"{A} obydwa dzieci to true")

        if (A.right != None and A.right.x == False and A.left != None and A.left.x == True) or \
            (A.right != None and A.right.x == True and A.left != None and A.left.x == False):
            all_to_cut += 1
            A.x = True
            print(f"{A} któreś z dzieci to False")

        if (A.right != None and A.right.x == False and A.left == None) or \
                (A.right == None and A.left != None and A.left.x == False):
            A.x = False
            print(f"{A} jednego dziecka nie ma a drugie to fałsz")

        if (A.right != None and A.right.x == True and A.left == None) or \
                (A.right == None and A.left != None and A.left.x == True):
            A.x = True
            print(f"{A} jednego dziecko nie ma a drugie to prawda")

        return

    max_lvl = 0
    for i in range(len(levels)):
        if levels[i] >= levels[max_lvl]:
            max_lvl = i

    print(f' dobry lvl to: {max_lvl}')
    cut_branches(T,max_lvl,0)
    return all_to_cut


# A = Node('A')
# B = Node('B')
# C = Node('C')
# A.left = B
# A.right = C
# D = Node('D')
# E = Node('E')
# B.left = D
# B.right = E
# F = Node('F')
# E.right = F
# G = Node('G')
# F.right = G

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
J = Node('J')
K = Node('K')
L = Node('L')
M = Node('M')
N = Node('N')
O = Node('O')
P = Node('P')
Q = Node('Q')
R = Node('R')
S = Node('S')
T = Node('T')

T.right = E

A.left =B
A.right = T

B.left = C
B.right = D

C.left =F
C.right = G

F.left = H
F.right = I

H.left = J
H.right = K

I.left = N
I.right = L

J.left = M
J.right = O

N.right = S

O.left = P
O.right = R

org = A
print(widentall(A))
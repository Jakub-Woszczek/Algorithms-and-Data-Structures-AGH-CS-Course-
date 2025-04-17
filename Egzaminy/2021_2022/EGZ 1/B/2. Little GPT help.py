class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.x = None

def widentall(T):
    levels = []

    # Funkcja rekurencyjna do znajdowania liczby węzłów na każdym poziomie
    def find_best_lvl(node, curr_lvl):
        if len(levels) < curr_lvl + 1:
            levels.append(1)
        else:
            levels[curr_lvl] += 1

        if node.left:
            find_best_lvl(node.left, curr_lvl + 1)
        if node.right:
            find_best_lvl(node.right, curr_lvl + 1)

    find_best_lvl(T, 0)

    # Znalezienie poziomu z największą liczbą węzłów (liści)
    max_lvl = 0
    for i in range(len(levels)):
        if levels[i] >= levels[max_lvl]:
            max_lvl = i

    all_to_cut = 0

    # Funkcja do usuwania niepotrzebnych gałęzi
    def cut_branches(node, max_lvl, curr_lvl):
        nonlocal all_to_cut

        if not node:
            return

        if curr_lvl == max_lvl:  # Jesteśmy na maksymalnym poziomie
            node.x = True
            return

        cut_branches(node.left, max_lvl, curr_lvl + 1)
        cut_branches(node.right, max_lvl, curr_lvl + 1)

        # Usunięcie dzieci, jeśli są poniżej maksymalnego poziomu
        if curr_lvl < max_lvl:
            if node.left and node.left.x != True:
                node.left = None
                all_to_cut += 1
            if node.right and node.right.x != True:
                node.right = None
                all_to_cut += 1

        # Ustawienie flagi `x` dla bieżącego węzła
        if (node.left and node.left.x) or (node.right and node.right.x):
            node.x = True
        else:
            node.x = False

    cut_branches(T, max_lvl, 0)

    return all_to_cut

A = Node()
B = Node()
C = Node()  # Ustawienie wartości 'C' w węźle C
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G

print(widentall(A))
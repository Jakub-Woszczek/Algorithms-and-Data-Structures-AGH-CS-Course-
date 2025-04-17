class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def ksum(T,k,p):
    def array_of_nodes_to_sorted_linked_list(T,k):
        # Tworzenie tablicy węzłów (Node) na podstawie wartości w T
        nodes = []
        i = 1
        for val in T:
            noodle = Node(val)
            nodes.append(noodle)

            if i == k:
                k_ty = noodle
            i += 1

        # Sortowanie tablicy węzłów (Node) według wartości
        nodes.sort(key=lambda node: node.val, reverse=True)  # Sortujemy malejąco

        # Tworzenie połączeń między węzłami w posortowanej tablicy
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]  # Każdy element wskazuje na następny

        # Ustawienie ostatniego elementu na None, aby oznaczyć koniec listy
        nodes[-1].next = None

        # Zwracamy głowę posortowanej listy i posortowaną tablicę węzłów
        return nodes[0], nodes  # Zwracamy głowę (pierwszy węzeł) i posortowaną tablicę węzłów

    def find_kth_element(head, k):
        current = head
        index = 1

        # Przemieszczamy się do k-tego elementu
        while current and index < k:
            current = current.next
            index += 1

        return current if current else None

    head,T_nodow_org= array_of_nodes_to_sorted_linked_list(T,k)
    k_ty = find_kth_element(head,k)

    print(k_ty.val)


T = [7,9,1,5,8,6,2,12]
k = 4
p = 5

ksum(T,k,p)

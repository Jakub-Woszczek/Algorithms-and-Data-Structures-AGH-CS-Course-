


# Funkcja pomocnicza do drukowania listy z oznaczeniem aktywnych węzłów
def print_linked_list(head):
    current = head
    while current:
        status = "A" if current.active else ""
        print(f"{current.val}{status} -> ", end="")
        current = current.next
    print("None")


# Funkcja sortująca listę jednokierunkową metodą Merge Sort



# Funkcja główna
def ksum(T, k, p):
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None
            self.active = False
    def Merge_sort(head):
        def merge_sort(head):
            if not head or not head.next:
                return head

            middle = get_middle(head)
            next_to_middle = middle.next
            middle.next = None

            left = merge_sort(head)
            right = merge_sort(next_to_middle)

            return merge(left, right)

        def get_middle(head):
            if not head:
                return head
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left

            if left.val > right.val:
                result = left
                result.next = merge(left.next, right)
                if result.next:
                    result.next.prev = result
            else:
                result = right
                result.next = merge(left, right.next)
                if result.next:
                    result.next.prev = result

            return result

        return merge_sort(head)
    all_zetki = 0
    n = len(T)

    # Tworzymy listę Node'ów
    T_noodles = [Node(val) for val in T]

    # Oznaczamy pierwsze p elementów jako aktywne
    for i in range(p):
        T_noodles[i].active = True

    # Sortowanie pierwszych p elementów malejąco
    T_first_sorted = sorted(T_noodles[:p], key=lambda node: node.val, reverse=True)

    # Tworzymy połączoną listę z tych elementów
    head = T_first_sorted[0]
    current = head
    for node in T_first_sorted[1:]:
        current.next = node
        node.prev = current
        current = current.next

    # Znajdujemy k-ty największy element (indeks k-1 po posortowaniu malejąco)
    k_ty = T_first_sorted[k - 1]

    # Dodajemy jego wartość do sumy
    all_zetki += k_ty.val

    # Przechodzimy po pozostałych przedziałach
    for i in range(p, n):
        print_linked_list(head)
        print(f"k-ty element to {k_ty.val}")

        # Węzeł do usunięcia (pierwszy element w bieżącym oknie)
        noodle_to_extract = T_noodles[i - p]

        # Węzeł do dodania (nowy element do okna)
        noodle_to_activate = T_noodles[i]
        noodle_to_activate.active = True

        # Usuwanie węzła z listy
        if noodle_to_extract.prev is None:  # Usuwany element jest głową
            head = noodle_to_extract.next
            if head:
                head.prev = None
        elif noodle_to_extract.next is None:  # Usuwany element jest końcem
            noodle_to_extract.prev.next = None
        else:  # Usuwany element jest w środku
            ancestor = noodle_to_extract.prev
            succesor = noodle_to_extract.next
            ancestor.next = succesor
            succesor.prev = ancestor

        # Dodanie nowego elementu do listy na właściwe miejsce
        current = head
        while current and current.val > noodle_to_activate.val:
            current = current.next

        if current is None:  # Dodajemy na koniec
            tail = head
            while tail.next:
                tail = tail.next
            tail.next = noodle_to_activate
            noodle_to_activate.prev = tail
        elif current == head:  # Dodajemy na początek
            noodle_to_activate.next = head
            head.prev = noodle_to_activate
            head = noodle_to_activate
        else:  # Dodajemy w środek
            prev_node = current.prev
            prev_node.next = noodle_to_activate
            noodle_to_activate.prev = prev_node
            noodle_to_activate.next = current
            current.prev = noodle_to_activate

        # Aktualizujemy k-ty element
        k_ty = head
        for _ in range(k - 1):
            k_ty = k_ty.next

        # Dodajemy wartość nowego k-tego elementu do sumy
        print(f"po zmianach dodaję {k_ty.val} do sumy")
        all_zetki += k_ty.val

    print(f"Znaleziono {k}-ty największy element: {k_ty.val}")
    return all_zetki


# Przykładowe dane wejściowe
T2 = [51, 56, 45, 6, 75, 52, 49, 58, 71, 36]
k2 = 2
p2 = 4

print("Wynik:", ksum(T2, k2, p2))

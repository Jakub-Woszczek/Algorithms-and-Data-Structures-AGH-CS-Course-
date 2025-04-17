class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.active = False

def print_linked_list(head):
    current = head
    while current:
        # Sprawdzamy, czy węzeł jest aktywny, i wypisujemy "A" obok wartości
        status = "A" if current.active else ""
        print(f"{current.val} {status} -> ",end="")
        current = current.next

def ksum(T, k, p):
    def Merge_sort(head):
        def merge_sort(head):
            # Jeśli lista jest pusta lub ma tylko jeden element, nie trzeba sortować
            if not head or not head.next:
                return head

            # Znajdź środek listy i podziel na dwie części
            middle = get_middle(head)
            next_to_middle = middle.next

            # Oddzielamy dwie połówki listy
            middle.next = None
            if next_to_middle:
                next_to_middle.prev = None

            # Rekurencyjnie sortujemy obie połowy
            left = merge_sort(head)
            right = merge_sort(next_to_middle)

            # Scal dwie posortowane połówki
            sorted_list = merge(left, right)

            return sorted_list

        def get_middle(head):
            # Znajdź środkowy element listy (funkcja slow-fast)
            if not head:
                return head

            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(left, right):
            # Tworzymy pusty "dummy" node jako punkt startowy
            if not left:
                return right
            if not right:
                return left

            # Sortujemy malejąco
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
    ilosc_w_przedziale = p
    T_noodles = [Node(val) for val in T]  # Tworze normalną tablice Nodów

    # Tworzenie pierwszych p elementów
    T_first = T_noodles[:p]
    for el in T_first:
        el.active = True  # Oznaczam je jako aktywne
    T_last = T_noodles[p:]  # Wydzielam resztę elementów
    T_first_sorted = sorted(T_first, key=lambda node: node.val, reverse=True)  # Sortowanie

    # Tworzenie posortowanej listy połączonej
    head = T_first_sorted[0]
    p = head
    for i in range(1, len(T_first_sorted)):  # Zrobienie ciągu z pierwszych p elementów
        noodle = T_first_sorted[i]
        p.next = noodle
        noodle.prev = p
        p = p.next
        if i + 1 == k:  # Znalezienie k-tego elementu
            k_ty = noodle

    # Dodawanie reszty elementów (nieaktywne)
    for noodle in T_last:
        p.next = noodle
        noodle.prev = p
        p = p.next

    # Merge sort całej listy, starting from head
    head = Merge_sort(head)
    all_zetki += k_ty.val

    # Dalsze operacje - np. aktywowanie kolejnych elementów
    for i in range(ilosc_w_przedziale, n):
        print_linked_list(head)
        print('')
        print(f'katy el to {k_ty.val}')
        noodle_to_extract = T_noodles[i - ilosc_w_przedziale]
        noodle_to_activate = T_noodles[i]

        # Tutaj nie zmienia się Node k_tego indexu
        if (noodle_to_activate.val > k_ty.val and noodle_to_extract.val > k_ty.val) or \
                (noodle_to_activate.val < k_ty.val and noodle_to_extract.val < k_ty.val):

            if noodle_to_extract.prev == None:
                succesor = noodle_to_extract.next
                noodle_to_extract.next = None
                succesor.prev = None
            # Usuwam już niepotrzebnego Noodela
            elif noodle_to_extract.next == None:  # Przypadek jak noodle jest na końcu
                noodle_to_extract.prev
                noodle_to_extract.next = None
                noodle_to_extract.prev = None

            else:
                ancestor = noodle_to_extract.prev
                succesor = noodle_to_extract.next

                ancestor.next = succesor
                succesor.prev = ancestor

            # Aktywuje nowego noodle
            noodle_to_activate.active = True

        # Usuwam większego, dodaje mniejszego
        elif noodle_to_extract.val > k_ty.val and noodle_to_activate.val < k_ty.val:

            # Usuwam już niepotrzebnego Noodela
            if noodle_to_extract.prev == None:
                succesor = noodle_to_extract.next
                noodle_to_extract.next = None
                succesor.prev = None

            elif noodle_to_extract.next == None: # Przypadek jak noodle jest na końcu
                noodle_to_extract.prev
                noodle_to_extract.next = None
                noodle_to_extract.prev = None

            else:
                ancestor = noodle_to_extract.prev
                succesor = noodle_to_extract.next

                ancestor.next = succesor
                succesor.prev = ancestor

            # Aktywuje nowego noodle
            noodle_to_activate.active = True

            k_ty = k_ty.next
            while k_ty.active != True:
                k_ty = k_ty.next





        # Usuwam mniejszego, dodaje większego
        else:
            # Usuwam już niepotrzebnego Noodela
            if noodle_to_extract.prev == None:
                succesor = noodle_to_extract.next
                noodle_to_extract.next = None
                succesor.prev = None

            elif noodle_to_extract.next == None:  # Przypadek jak noodle jest na końcu
                noodle_to_extract.prev
                noodle_to_extract.next = None
                noodle_to_extract.prev = None

            else:
                ancestor = noodle_to_extract.prev
                succesor = noodle_to_extract.next

                ancestor.next = succesor
                succesor.prev = ancestor

                # Aktywuje nowego noodle
                noodle_to_activate.active = True

            k_ty = k_ty.prev
            while k_ty.active != True:
                k_ty = k_ty.prev

        print(f'po zmianach dodaje do all {k_ty.val}')
        all_zetki += k_ty.val
        # print(f'dpdałem {k_ty.val}')




    print(f"Znaleziono {k}-ty największy element: {k_ty.val}")
    return all_zetki

# Przykładowe dane wejściowe
T = [7, 9, 1, 5, 8, 6, 2, 12]
k = 4
p = 5
T2 =  [51, 56, 45, 6, 75, 52, 49, 58, 71, 36]
k2 =  2
p2 =  4
# Prawidlowy wynik:	 385
print(ksum(T2, k2, p2))

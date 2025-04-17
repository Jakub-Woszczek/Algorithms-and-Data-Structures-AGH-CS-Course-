def ksum(T,k,p):
    class Node():
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

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

    def create_T_of_Nodes(T):
        T_of_nodes = []

        for el in T:
            T_of_nodes.append(Node(el))

        return T_of_nodes

    T_of_nodes = create_T_of_Nodes(T)
    suma_ztek = 0

    def create_primal_sorted_linked_list(T_of_N):
        head = T[0]
        p = head

        for i in range(1,len(T_of_N)):
            node = T_of_N[i]
            p.next = node
            node.prev = p
            p = p.next

        head = Merge_sort(head)

        return head

    def ustaw_k_ty(head, k):
        k_ty = None

        while k > 1:
            head = head.next
            k -= 1
        k_ty = head
        return k_ty

    def add_and_extract(node_to_add,node_to_extract,k_ty):

        # if node_to_add.val > k_ty.val and node_to_extract.val + k_ty.val:
        return





    head = create_primal_sorted_linked_list(T_of_nodes[:p])
    k_ty = ustaw_k_ty(head,k)
    suma_ztek += k_ty.val






    # print(T_first)
    return

T = [7,9,1,5,8,6,2,12]
k = 4
p = 5

ksum(T,k,p)
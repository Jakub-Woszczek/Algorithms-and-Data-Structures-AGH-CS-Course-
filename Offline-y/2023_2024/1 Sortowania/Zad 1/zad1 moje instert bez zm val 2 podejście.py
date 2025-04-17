
class Node():

    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def fromarr(arr):
    p = None
    for v in reversed(arr): # iterowanie przez tablicę w odwrotnym kierunku
        p = Node(v, p)
    return p


def SortH(p,k):
    p_org = p
    indicator = 1
    while indicator == 1:
        p_prev = None
        p = p_org
        if p.val > p.next.val:  # Biore z początku
            p_search = p.next
            p_org = p.next
            p.next = None
            while p_search != None and p_search.val < p.val:
                p_search_prev = p_search
                p_search = p_search.next

            if p_search != None:  # Na środek
                p_search_prev.next = None
                p_search_prev.next = p
                p.next = p_search
                indicator += 1
            else:  # Na koniec
                p_search_prev.next = p
                indicator += 1

        else:  # szukam złego el na środku
            p_prev = p
            p = p.next
            while p.next != None and p.val < p.next.val:  # Szukam złego na środku
                p_prev = p
                p = p.next

            if p.next == None:
                return p_org

            p_prev.next = None  # Wycinam zły element
            p_search = p.next
            p.next = None
            p_prev.next = p_search
            p_search_prev = None
            while p_search != None and p_search.val < p.val:  # Szukam dobrego miejsca
                p_search_prev = p_search
                p_search = p_search.next

            if p_search != None:  # Daje na środek
                p_search_prev.next = None
                p_search_prev.next = p
                p.next = p_search
                indicator += 1

            else:  # Daje na koniec
                p_search_prev.next = p
                indicator += 1

        if indicator == 1:
            return p_org

        indicator = 1

    return p_org
        # while p.next != None:

lsit = [2,3,10,4,1,5,8,6,9]
head = fromarr(lsit)
print_linked_list(SortH(head,1))

########
def sort(p):
    p_org = p
    indicator = 1
    while indicator == 1:
        p_prev = None
        p = p_org
        if p.val > p.next.val:  # Biore z początku
            p_search = p.next
            p_org = p.next
            p.next = None
            while p_search != None and p_search.val < p.val:
                p_search_prev = p_search
                p_search = p_search.next

            if p_search != None:  # Na środek
                p_search_prev.next = None
                p_search_prev.next = p
                p.next = p_search
                indicator += 1
            else:  # Na koniec
                p_search_prev.next = p
                indicator += 1

        else:  # szukam złego el na środku
            p_prev = p
            p = p.next
            while p.next != None and p.val < p.next.val:  # Szukam złego na środku
                p_prev = p
                p = p.next

            if p.next == None:
                return p_org

            p_prev.next = None  # Wycinam zły element
            p_search = p.next
            p.next = None
            p_prev.next = p_search
            p_search_prev = None
            while p_search != None and p_search.val < p.val:  # Szukam dobrego miejsca
                p_search_prev = p_search
                p_search = p_search.next

            if p_search != None:  # Daje na środek
                p_search_prev.next = None
                p_search_prev.next = p
                p.next = p_search
                indicator += 1

            else:  # Daje na koniec
                p_search_prev.next = p
                indicator += 1

        if indicator == 1:
            return p_org

        indicator = 1

    return p_org
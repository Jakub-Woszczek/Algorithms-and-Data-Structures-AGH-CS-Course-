import random


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

def SortH(p, k): # 2 podejście

    def sort(p):
        if p.next == None:
            return p
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

    a = k
    p_org = p
    p_org_1 = p_org
    i = 2 * a + 1
    while i > 1 and p.next != None:
        p = p.next
        i -= 1
    p_end_2 = p.next
    p.next = None
    # Sortuj p_org gdzie p_end_1 to head
    p_org = sort(p_org)
    p_end_1 = p_org_1
    p_org_1 = p_end_1
    while p_end_1.next != None:
        p_end_1 = p_end_1.next
    p_end_1.next = p_end_2
    p_end_1 = p_end_1.next
    while p_end_2.next != None:
        a=k
        while a > 0:
            p_end_1 = p_end_1.next
            p_org_1 = p_org_1.next
            a-=1
        p_org_2 = p_org_1.next
        p_end_2 = p_end_1.next

        p_org_1.next = None
        p_end_1.next = None
        # Sort p_org_2 gdzie head to poczatek
        head = sort(p_org_2)
        # head = p_org_2
        head_org = head
        while head.next != None:
            head = head.next
        p_org_1.next = head_org
        head.next = p_end_2

    p_org_1 = p_org_1.next
    p_org_2 = p_org_2.next
    p_org_1.next = None
    # Sortujemy p org 1 początek to head
    head = sort(p_org_2)

    p_org_1.next = head

    return p_org










# def SortH(p, k): # 1 podejście
#
#
#     a = k
#     p_org = p
#     i = 2 * a + 1
#     while i > 1:
#         p = p.next
#         i-=1
#     p_org_2 = p.next
#     p.next = None
#     p = p_org_2
#     head = p_org # Tu sort
#     while head.next != None:
#         head = head.next
#     head.next = p
#     while a >0:
#         p_org = p_org.next
#         a-=1

lsit =[2,1,3,5,4,7,6]
head = fromarr(lsit)
print_linked_list(SortH(head,1))
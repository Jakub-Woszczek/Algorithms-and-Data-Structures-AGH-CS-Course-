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


def SortH(p, k):
    p_org = p
    while True:
        p_prev = None
        while p.next !=None:
            if p.val > p.next.val and p_prev == None:  # Kod przenosi 1st el gdzieś
                p_1 = p.next
                p.next = None
                p_1_org = p_1
                while p_1.val < p.val:
                    p_1_prev = p_1
                    p_1 = p_1.next
                p_1_prev.next = None
                p_1_prev.next = p
                p.next = p_1
                p = p_1_org

            else:
                if p.val > p.next.val:
                    p_1 = p.next
                    if p_prev == None:
                        p.next = None
                        while p_1.val < p.val:
                            p_1_prev = p_1
                            p_1 = p_1.next
                    else:
                        p.next = None
                        p_prev.next = p_1
                        while p_1 != None and  p_1.val < p.val:
                            p_1_prev = p_1
                            p_1 = p_1.next
                        if p_1 == None:
                            p_1_prev.next = p
                        else:
                            p_1_prev.next = None
                            p_1_prev.next = p
                            p.next = p_1


            p_prev = p
            p = p.next


    return p_org

lsit = [1,2,3,9,4,5,7,8]
head = fromarr(lsit)
print(SortH(head,1))
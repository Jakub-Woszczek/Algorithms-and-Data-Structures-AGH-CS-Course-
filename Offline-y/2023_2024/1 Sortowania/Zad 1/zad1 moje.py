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
    indicator = 2
    last_sorted = float("inf")
    st_round = 0
    last_sorted_prev = float("inf")
    while indicator != 1:
        p1 = p
        if st_round == 0:
            if p.next != None:
                p2 = p.next
                if p.next != None:
                    p3 = p.next.next
                else:
                    p3 = p.next

        i = 0
        indicator = 1
        p = p_org
        while (p.next != None and i<last_sorted_prev) or (st_round ==0 and p.next != None):
            if p.next.val<p.val:
                # p.next.val, p.val = p.val, p.next.val
                p1.next= None
                p.next= None
                p2.next = None
                p1.next, p.next = p2,p3
                p2.next = p

                indicator += 1
                last_sorted = i+1
            p1 = p
            p = p.next
            p2 = p2.next
            p3 = p3.next
            i+=1
            p , p2 = p2, p
        st_round +=1
        last_sorted_prev = last_sorted



    return p_org

list = [random.randint(1,1000) for _ in range(1,10)]
head = fromarr(list)
print_linked_list(head)

head_sorted = SortH(head,1)
print_linked_list(head_sorted)




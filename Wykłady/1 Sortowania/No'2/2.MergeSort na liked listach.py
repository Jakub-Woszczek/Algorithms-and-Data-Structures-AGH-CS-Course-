class Node():
    def __init__(self,val,next = None):
        self.next = next
        self.val = val

def MergeSort(head):
    head_org = head
    mid = head

    if head == None or head.next == None:
        return head

    while head.next != None and head.next.next != None:
        head = head.next.next
        mid = mid.next
    link = mid.next
    mid.next = None
    link_1 = MergeSort(head_org)
    link_2 = MergeSort(link)

    return Scal(link_1,link_2)


def Scal(a,b):
    c = Node(None)
    c_org = c
    while a != None and b != None:
        if a.val < b.val:
            c.next = a
            a=a.next
            c.next.next = None
            c=c.next
        else:
            c.next = b
            b = b.next
            c.next.next = None
            c = c.next

    if a == None:
        while b != None:
            c.next = b
            b = b.next
            c.next.next = None
            c = c.next
    else:
        while a != None:
            c.next = a
            a = a.next
            c.next.next = None
            c = c.next

    c_org = c_org.next

    return c_org

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
import random
head = fromarr([random.randint(1,1000) for _ in range(10)])
print_linked_list(head)
head_sorted = MergeSort(head)
print_linked_list(head_sorted)
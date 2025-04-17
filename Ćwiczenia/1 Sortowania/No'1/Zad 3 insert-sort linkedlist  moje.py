class Node():
    def __init__(self,val,next = None):
        self.next = None
        self.val = val

def insert_sort(head):
    if head.next == None or head.next.next == None:
        return head

    unsorted = head.next.next
    head.next.next = None
    while unsorted != None:
        next = unsorted.next
        insert(head,unsorted)
        unsorted = next
    return head

def insert(list,node):

    if list.next == None:
        list.next = node
        node.next = None
        return
    elif list.next.val > node.val:
        tail = list.next
        list.next = node
        node.next = tail
        return
    insert(list.next,node)


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

head = fromarr([5,4,3,2,1])
print_linked_list(insert_sort(head))
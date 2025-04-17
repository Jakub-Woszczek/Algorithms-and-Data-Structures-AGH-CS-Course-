class Node():
    def __init__(self,val,next = None):
        self.next = next
        self.val = val

def insert_sort(head):
    sorted_org = head
    srted = head
    unsorted = head.next

    while unsorted != None:
        if unsorted.val < srted.val:
            unsorted_v2 = unsorted.next

            if unsorted.val<sorted_org.val:     # if jezeli idzie na poczatek
                srted.next = None
                unsorted.next = None
                srted.next = unsorted_v2
                unsorted.next = sorted_org
                sorted_org = unsorted



            search = sorted_org

            while search.next.val < unsorted.val:
                search = search.next
            search_v2 = search.next
            search.next = None
            srted.next = None
            unsorted.next = None
            srted.next = unsorted_v2
            search.next = unsorted
            unsorted.next = search_v2
            unsorted = unsorted_v2

        else:
            unsorted = unsorted.next
            srted = srted.next



    return sorted_org

# def insert(list,node):



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

head = fromarr([5,10,1,2,3,4,9,6,7,8])
print_linked_list(head)
head_sorted = insert_sort(head)
print_linked_list(head_sorted)
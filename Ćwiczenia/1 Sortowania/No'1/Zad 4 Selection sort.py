class Node():
    def __init__(self,val,next = None):
        self.next = next
        self.val = val

def sel_sort(T):
    srted = Node(None)
    while T.next != None:
        smallest = float("inf")
        mlast = None
    while A != None:
        if A.val < smallest:
            smallest = A.val
            mlast = last
        last = A
        A = A.next
    B.next = mlast.next
    B = B.next
    mlast.next = mlast.next.next

# Rwwwaa ale syf
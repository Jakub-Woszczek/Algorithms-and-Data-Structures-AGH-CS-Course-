class Node():

    def __init__(self,val,left = None,right = None):
        self.val = val
        self.right = None
        self.left = None

def maxrank(T):

    n = len(T)
    root = Node(T[0])

    def add_node(p, val):

        if val < p.val:

            if p.left == None:
                new = Node(val)
                p.left = new
                return

            else:
                add_node(p.left, val)

        else:

            if p.right == None:
                new = Node(val)
                p.right = new
                return

            else:
                add_node(p.right, val)
        return

    for i in range(1,n):
        add_node(root,T[i])

    def search_longest(p,strike):

        max_strike = 0

        if p.left == None and p.right == None:
            return strike

        if p.left != None:
            max_strike = max(max_strike,search_longest(p.left,strike+1))

        if p.right != None:
            max_strike = max(max_strike,search_longest(p.right,strike))

        return max_strike

    return search_longest(root,1)

T = [9,3,6,5,8,2,1,3,8,5,9,5,11,8,7,6,5,4]
print(maxrank(T))
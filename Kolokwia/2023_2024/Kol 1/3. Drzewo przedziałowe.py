class Node():

    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left_amnt = 0
        self.right_amnt = 0
        self.right = None
        self.left = None
        self.self_amnt = 1

def maxrank(T):

    n = len(T)
    root = Node(T[0])

    def add_node(p,val):

        # 1.To ten sam,
        # 2.idzie na strone i nie ma tam
        # 3. idzie na strone i zajęte

        if val == p.val:
            p.self_amnt += 1

            return

        if val < p.val:

            if p.left == None:
                new = Node(val)
                p.left = new
                p.left_amnt += 1
                return

            else:
                p.left_amnt += 1
                add_node(p.left,val)

        else:

            if p.right == None:
                new = Node(val)
                p.right = new
                p.right_amnt += 1
                return

            else:
                p.right_amnt += 1
                add_node(p.right, val)

        return

    for i in range(1,n):
        add_node(root,T[i])


    return

T = [5,3,9,4,3,6,31,6,74,5,14,6,3]
maxrank(T)




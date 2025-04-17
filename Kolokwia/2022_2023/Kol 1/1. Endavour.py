class Node():

    def __init__(self,val,index):
        self.val = val
        self.right = None
        self.right_amnt = 0
        self.left = None
        self.left_amnt = 0
        self.index = index

def ksum(T, k, p):

    def add_node(root,node):

        p = root
        if node.val < p.val:
            p.left_amnt += 1

            if p.left == None:
                p.left = node
            else:
                add_node(p.left,node)

        else:
            p.right_amnt += 1

            # if p.right


    def create_primal_tree(T):

        root = Node(T[0],0)

        for i in range(1,len(T)):
            node = Node(T[i],i)
            i += 1


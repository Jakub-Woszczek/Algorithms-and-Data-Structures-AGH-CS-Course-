class Node():

    def __init__(self,val,left = None,right = None):
        self.val = val
        self.right = None
        self.left = None
        self.left_amnt = 0


def maxrank(T):

    n = len(T)
    root = Node(T[0])
    bigger_than = [0]*n


    def add_node(p,val,i):

        if val < p.val:
            p.left_amnt += 1

            if p.left != None:
                add_node(p.left,val,i)

            else:
                p.left = Node(val)

        else:
            if val != p.val:
                bigger_than[i] += 1+p.left_amnt
            else:
                bigger_than[i] += p.left_amnt

            if p.right != None:
                add_node(p.right,val,i)

            else:
                p.right = Node(val)


    for i in range(1,n):
        add_node(root,T[i],i)

    print(bigger_than)

    return max(bigger_than)




T = [9, 3, 6, 5, 8, 2, 1, 3, 8 , 5, 9, 5, 11 , 8, 7, 6, 5, 4]
T2 = [5,3,9,4]
print(maxrank(T))
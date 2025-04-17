#We merge here two sorted arrays
class Node():
    def __init__(self,val,next=None):
        self.next = None
        self.val = None

def merge(head1,head2):
    warden = Node()
    warden_org = warden
    while head1 is not None and head2 is not None:
        if head1.val < head2.val:
            warden.next = head1
            head1 = head1.next
            warden = warden.next
        else:
            warden.next = head2
            warden = warden.next
            head2 = head2.next
    if head1 is None:
        warden.next = head2
    else:
        warden.next = head1
    return warden_org.next


#Dzielimy na 2 podciągi

def get_series(p):
    if p == None:
        return None,None
    else:
        current = p
        while current.next is not None and warden.val <=warden.next.val:
            current = current.next
        tnp = current.next
        current.next = None
        return p,tnp

#Robimy sorta

def getSeriesLight(p):
    head = Node()
    head.val,p = get_series(p)
    i = head
    while p!= None:
        i.next = Node()
        i = i.next
        i.val,p = get_series(p)
    return head

def sort(p):
    blocks = getSeriesLight(p)
    while blocks.next != None:
        p1 = blocks
        p2 = p1.next
        while p2 != None:
            merge(p1.val,p2.val)
        p1.next = p2.next
        p1 = p1.next
        if p1 != None:
            p2 = p2.next
        else:
            break
    return blocks


# def sort(p):

class Node:
    def __init__( self, val ):
        self.next = None
        self.val = val

def tasks(T):
    def how_long(p):

        i = 1
        while p.next != None:
            p = p.next
            i += 1
        return i

    def insert(wartownik, wensel):
        # Zakładamy, że wartownik jest sztucznym elementem (strażnikiem)
        p = wartownik

        # Przesuwamy wskaźnik, dopóki p.next istnieje i p.next.val[0] < wensel.val[0]
        while p.next is not None and p.next.val[0] < wensel.val[0]:
            p = p.next

        # Wstawiamy wensel między p a p.next
        wensel.next = p.next
        p.next = wensel

        return wartownik

    def merge(p1,p2):

        guard = Node(None)  # Strażnik (wartownik)
        p = guard  # Wskaźnik, który będzie przechodził po nowej liście

        # Główna pętla łącząca obie listy, dopóki obie nie będą puste
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p.next = p1  # Dołącz p1 do wyniku
                p1 = p1.next  # Przesuwamy wskaźnik w p1
            else:
                p.next = p2  # Dołącz p2 do wyniku
                p2 = p2.next  # Przesuwamy wskaźnik w p2
            p = p.next  # Przesuwamy wskaźnik wynikowy

        # Dołącz pozostałe elementy (jeśli któryś z list nie jest pusty)
        if p1 is not None:
            p.next = p1
        elif p2 is not None:
            p.next = p2

        return guard.next

    def linked_na_list(p):
        T = []
        p = p.next
        while p != None:
            T.append(p.val)
            p = p.next

        return T


    wartownik = Node(None)
    wartownik_org = wartownik
    i = 0
    for p in T:

        lenght = how_long(p)
        wensel = Node((lenght,p))
        if i == 0:
            wartownik.next = wensel
        else:
            insert(wartownik,wensel)

        i += 1

    while wartownik.next.next != None:

        p1,p2 = wartownik.next, wartownik.next.next
        wartownik.next = p2.next
        p1.next,p2.next = None, None

        p = merge(p1,p2)
        insert(wartownik,p)

    tablica = linked_na_list(wartownik)
    return tablica

T = [[0,1,2,4,5],[0,10,20],[5,15,25]]
print(tasks(T))

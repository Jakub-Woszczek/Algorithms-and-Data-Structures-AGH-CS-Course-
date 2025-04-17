from zad3testy import runtests
class Node:
    def __init__( self, val ):
        self.next = None
        self.val = val

    
def tasks(T):
    def merge(p1, p2):

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

    p = T[0]

    for i in range(1, len(T)):
        p1 = T[i]
        p = merge(p, p1)

    return p
    return [i for i in range(len(T))]  # domyslny wynik [0,1,2,... ]



runtests( tasks )

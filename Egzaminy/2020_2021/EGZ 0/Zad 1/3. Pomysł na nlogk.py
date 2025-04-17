class Node():

    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def tanagram(x, y, t):
    def czy_posortowana(tablica):
        return tablica == sorted(tablica)
    def indeksy_wystapien(slowo):
        T = [[None] for _ in range(26)]
        odwiedzone = []

        i = 0
        for litera in slowo:
            index = ord(litera) - 97
            T[index].append(i)
            i += 1

        return T

    T = indeksy_wystapien(x)

    def mirror_indexes(org,new_word):
        T_new = []
        for letter in new_word:
            index = ord(letter)-97

            i = 0
            while org[index][i] == None and i < len(org[index])-1:
                i += 1
            T_new.append(org[index][i])
            org[index][i] = None

        return T_new

    T_vol2 = mirror_indexes(T,y)

    def buble_sort(napis,iteracje):

        for _ in range(iteracje):
            for  i in range(len(napis)-1):

                if napis[i] > napis[i+1]:
                    napis[i],napis[i+1] = napis[i+1],napis[i]

        return napis

    k_sortow = buble_sort(T_vol2,t)

    return czy_posortowana(k_sortow)








print(tanagram('','tokmysoz',3))

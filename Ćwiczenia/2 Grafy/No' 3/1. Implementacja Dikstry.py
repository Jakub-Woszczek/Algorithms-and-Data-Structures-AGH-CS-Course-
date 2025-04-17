# Używam kolejki pythonowskiej
from queue import PriorityQueue
# put((_,_))
# get() = (_,_)
# distance

def dikjstra(Graph,start,distacne):
    # Tutaj na tablicy distance dodajemy odlegość wierzchołka o indexie
    # 'start' na 0
    distacne[start] = 0
    queue = PriorityQueue()
    # Tutaj dodajemy do kolejki priorytetowej tupla - (dystans,vierchułek)
    queue.put((0,start))

    # Tutaj warun jak kolejka będzie pusta
    while not queue.empty():
        # Tutaj ściągamy pierwszy wierchułek i v - index wierchułka
        v = queue.get()[1]

        # Robimy pętelke po somsiadach v
        for neighbor in Graph[v]:
            u = neighbor[0] # Tutaj mamy dystans somsiada
            d = neighbor[1] # Tutaj mamy index somsiada
            # Tutaj mamy waruna że jeżeli już mamy jakiś dystans
            # zapisany na tym wierzchołku to porównujemy go do
            # nowej drogi
            if distacne[u] > distacne[v] + d:
                distacne[u] = distacne[v] + d
                queue.put((distacne[u],u))
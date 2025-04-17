# Mamy graf z wagami w postaci liczb rzeczywistych, prosze zaproponować algo
# znajdujący scieżkę o najmniejszym iloczynie krawędzi

def zad2(G):
    topo = topologicalSort(G)
    distances = [inf]*len(G)
    distances[0]=0
    for v in topo:
        for u,w in  enumerate(c,[v]):
            distances[u] = min(distances[u],distances[v] + w)

    return distances
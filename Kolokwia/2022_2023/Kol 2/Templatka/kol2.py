from kol2testy import runtests

def beautree(G):
    def edges_from_graph(G):
        edges = []
        visited = set()

        for u in range(len(G)):
            for v, weight in G[u]:
                if (v, u) not in visited:
                    edges.append((u, v, weight))
                    visited.add((u, v))

        return edges

    G_edges = edges_from_graph(G)
    G_edges.sort(key=lambda x: x[2])  # Sortujemy krawędzie po wadze
    n = len(G)
    Included = [False for _ in range(n)]
    All_Included = n
    MST_sum = 0
    colors = [-1 for _ in range(n)]
    color = 0

    for v1, v2, edge in G_edges:
        # Jeśli wszystkie wierzchołki są zajęte, sprawdzamy spójność
        if All_Included < 1:
            color_sample = colors[0]
            flag = False
            for i in range(1, n):
                if colors[i] != color_sample:  # Jeśli którykolwiek wierzchołek ma inny kolor
                    flag = True

            if not flag:  # Jeśli wszystkie wierzchołki są tego samego koloru, kończymy
                break
            # else:

        # Nowy kolor - jeśli oba wierzchołki są nowe
        if Included[v1] == False and Included[v2] == False:
            color += 1
            Included[v1], Included[v2] = True, True
            colors[v1], colors[v2] = color, color
            MST_sum += edge
            All_Included -= 2

        # Rozszerzenie koloru, gdzie v1 jest nowym wierzchołkiem
        if Included[v1] == False and Included[v2] == True:
            extended_color = colors[v2]
            colors[v1] = extended_color
            Included[v1] = True
            MST_sum += edge
            All_Included -= 1

        # Rozszerzenie koloru, gdzie v2 jest nowym wierzchołkiem
        if Included[v1] == True and Included[v2] == False:
            extended_color = colors[v1]
            colors[v2] = extended_color
            Included[v2] = True
            MST_sum += edge
            All_Included -= 1

        # Łączenie dwóch różnych kolorów (spójne komponenty)
        if Included[v1] == True and Included[v2] == True and colors[v1] != colors[v2]:
            color_supreme = colors[v1]
            color_inferior = colors[v2]
            for i in range(n):
                if colors[i] == color_inferior:
                    colors[i] = color_supreme

            MST_sum += edge

        # Wykrycie cyklu (jeśli oba wierzchołki mają ten sam kolor)
        if Included[v1] == True and Included[v2] == True and colors[v1] == colors[v2]:
            continue

    return MST_sum
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )

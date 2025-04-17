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
            print(f'Juz stworzylem MST. Sprawdzam spójność drzewa.')
            color_sample = colors[0]
            flag = False
            for i in range(1, n):
                print(f'Sprawdzam wierzchołek {i}: kolor {colors[i]}, oczekiwany kolor {color_sample}')
                if colors[i] != color_sample:  # Jeśli którykolwiek wierzchołek ma inny kolor
                    print(f'Wierzchołek {i} ma inny kolor ({colors[i]}), flag ustawiony na True')
                    flag = True

            if not flag:  # Jeśli wszystkie wierzchołki są tego samego koloru, kończymy
                print(f'Wszystkie wierzchołki są tego samego koloru ({color_sample}), kończę.')
                break
            else:
                print(f'Nie wszystkie wierzchołki mają ten sam kolor, kontynuuję dodawanie krawędzi.')

        # Nowy kolor - jeśli oba wierzchołki są nowe
        if Included[v1] == False and Included[v2] == False:
            print(f'Nowy kolor przed : {colors} ')
            color += 1
            Included[v1], Included[v2] = True, True
            colors[v1], colors[v2] = color, color
            MST_sum += edge
            All_Included -= 2
            print(f'Nowy kolor po : {colors} ')
            print('')

        # Rozszerzenie koloru, gdzie v1 jest nowym wierzchołkiem
        if Included[v1] == False and Included[v2] == True:
            print(f'Extend kolor przed : {colors} ')
            extended_color = colors[v2]
            colors[v1] = extended_color
            Included[v1] = True
            MST_sum += edge
            All_Included -= 1
            print(f'Extend kolor po : {colors} ')
            print('')

        # Rozszerzenie koloru, gdzie v2 jest nowym wierzchołkiem
        if Included[v1] == True and Included[v2] == False:
            print(f'Extend kolor przed : {colors} ')
            extended_color = colors[v1]
            colors[v2] = extended_color
            Included[v2] = True
            MST_sum += edge
            All_Included -= 1
            print(f'Extend kolor po : {colors} ')
            print('')

        # Łączenie dwóch różnych kolorów (spójne komponenty)
        if Included[v1] == True and Included[v2] == True and colors[v1] != colors[v2]:
            print(f'Merge kolor przed : {colors} ')
            color_supreme = colors[v1]
            color_inferior = colors[v2]
            for i in range(n):
                if colors[i] == color_inferior:
                    colors[i] = color_supreme

            MST_sum += edge
            print(f'Merge kolor po : {colors} ')
            print('')

        # Wykrycie cyklu (jeśli oba wierzchołki mają ten sam kolor)
        if Included[v1] == True and Included[v2] == True and colors[v1] == colors[v2]:
            print(f'Cykl wykryty między wierzchołkami {v1} i {v2}. Krawędź pominięta.')
            continue

    return MST_sum




G = [ [(1,3), (2,1), (4,2)], # 0
[(0,3), (2,5) ], # 1
[(1,5), (0,1), (3,6)], # 2
[(2,6), (4,4) ], # 3
[(3,4), (0,2) ] ] # 4
G2 = [[(1, 2), (2, 3)], [(0, 2), (2, 1), (3, 5), (4, 6)], [(0, 3), (1, 1), (3, 9), (4, 4)], [(1, 5), (2, 9), (4, 10), (5, 8)], [(2, 4), (1, 6), (3, 10), (5, 7)], [(3, 8), (4, 7)]]
E2 = [[(1, 633), (2, 849), (3, 1218), (4, 2550)], [(0, 633), (4, 362)], [(0, 849), (3, 21), (4, 3044)], [(0, 1218), (2, 21)], [(0, 2550), (1, 362), (2, 3044)]]


print(beautree(E2))
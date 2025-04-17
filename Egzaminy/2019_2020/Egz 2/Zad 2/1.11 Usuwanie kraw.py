def usuwanie_kraw(is_edge_occupied, vertex_edges_connected, is_vertes_ocuppied, Edges_sorted, min_edge, max_edge):
    # Ten algo ma usunąć min kraw i spr czy is_vertes_ocuppied brakuje coś
    # i jak brakuje to dodawać następne

    # is_edge_occupied, vertex_edges_connected, is_vertes_ocuppied, Edges_sorted., min edge, max edge

    # Pierwyj trza is_edge_occupied zmienić
    # Późni trza vertex_edges_connected zmienić
    # Późni trza zmienić min_curr_v
    # Późni trza dodawać winksze póki  is_vertes_ocuppied full

    i = 0
    while i < len(is_edge_occupied)-1: # Mam index min kraw
        if is_vertes_ocuppied[i] == True:
            break
        i += 1
    edge_to_del = i
    is_vertes_ocuppied[i] = False

    v1,v2,dist,ids = Edges_sorted[i]
    for i in range(len(vertex_edges_connected[v1])):
        if len(vertex_edges_connected[v1]) == 1:
            is_vertes_ocuppied[v1] = False
            vertex_edges_connected[v1] = None
            min_edge = Edges_sorted[edge_to_del + 1][3]

            # Tutaj trza kod na szukanie kraw
            # while are_all_connected()

        else:
            if vertex_edges_connected[v1][i] == edge_to_del:
                del vertex_edges_connected[v1][i]
            min_edge = Edges_sorted[edge_to_del + 1][3]

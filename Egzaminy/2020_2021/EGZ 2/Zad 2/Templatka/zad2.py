from zad2testy import runtests


def balance( T ):
    def add_childs_val(T):

        if len(T.edges) < 1:
            return 0


        all_children = 0
        for i in range(len(T.edges)):
            branch = T.weights[i] + add_childs_val(T.edges[i])

            T.weights[i] = [T.weights[i],branch]

            all_children += branch

        return all_children

    all_edges_sum = 0
    add_childs_val(T)
    for i in range(len(T.edges)):
        all_edges_sum += T.weights[i][1]


    diff_min = float('inf')
    ids_min = None
    def search_for_right_one(T,upfront,id_upfront):
        nonlocal diff_min
        nonlocal ids_min

        n = len(T.edges)

        if n < 1:
            return

        children_sum = 0
        if n >= 1:
            for i in range(n):
                children_sum += T.weights[i][1]

        # Teraz szukam diff jeżeli bym odciął poprzednią krawędź
        diff = abs((all_edges_sum - children_sum - upfront) - children_sum)
        if diff < diff_min:
            diff_min = diff
            ids_min = id_upfront
        diff_min = min(diff_min,diff)


        for i in range(n):
            search_for_right_one(T.edges[i],T.weights[i][0],T.ids[i])

    for i in range(len(T.edges)):
        V_1 = all_edges_sum - T.weights[i][1] # Cała reszta bez kraw i jej dzieci
        V_2 = T.weights[i][1] - T.weights[i][0]

        diff  = abs(V_1 - V_2)
        if diff < diff_min:
            diff_min = diff
            ids_min = T.ids[i]

        search_for_right_one(T.edges[i],T.weights[i][0],T.ids[i])

    print(diff_min)
    print(ids_min)

    return ids_min
    return -1

    
runtests( balance )



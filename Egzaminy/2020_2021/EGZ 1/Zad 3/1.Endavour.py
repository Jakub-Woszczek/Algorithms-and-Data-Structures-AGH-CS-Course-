def kintersect( A, k ):
    def sort_coordinates(points):
        # Ekstrahuj współrzędne x i y
        x_coords = [x for x, y in points]
        y_coords = [y for x, y in points]

        # Sortuj współrzędne x i y
        sorted_x_coords = sorted(x_coords)
        sorted_y_coords = sorted(y_coords)

        return sorted_x_coords, sorted_y_coords

    x_sorted,y_sorted = sort_coordinates(A)

    x_i,y_i = 0,0

def tower_builder(n_floors):
        lst = []
        i = 1
        count_floors = 1
        width = n_floors * 2 - 1
        while count_floors <= n_floors:
            lst.append(("*" * i).center(width))
            i += 2
            count_floors += 1
        return lst
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

# 2  case
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
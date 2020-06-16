def convert_cartesian(x, y):
    tx = [(el,) for el in x]
    ty = [(el,) for el in y]
    c = [tx[i] + ty[i] for i in range(len(tx))]
    return c


print(convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]))
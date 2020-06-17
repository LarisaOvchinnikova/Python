def convert_cartesian(x, y):
    return [(x[i], y[i]) for i in range(len(x))]


print(convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]))
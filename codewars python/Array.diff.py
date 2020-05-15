def array_diff(a, b):
    return [el for el in a if b.count(el) == 0]
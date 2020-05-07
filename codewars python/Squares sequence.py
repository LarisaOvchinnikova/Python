def squares(x, n):
    lst = []
    p = x
    for i in range(n):
        lst.append(p)
        p = p * p
    return lst
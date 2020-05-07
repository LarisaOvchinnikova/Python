def squares(x, n):
    lst = []
    p = x
    for i in range(n):
        lst.append(p)
        p = p * p
    return lst

# ---- 2 case
def squares(x, n):
    return [x ** (2 ** i)  for i in range(n)]
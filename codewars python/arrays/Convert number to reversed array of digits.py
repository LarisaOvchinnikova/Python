def digitize(n):
    lst = list(str(n)[::-1])
    res = [int(el) for el in lst]
    return res
print(digitize(35231))
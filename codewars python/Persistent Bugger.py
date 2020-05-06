def persistence(n):
    count = 0
    n = str(n)
    p = 1
    while len(n) > 1:
        for i in n:
            p = p * int(i)
        n = str(p)
        count += 1
        p = 1
    return count
def digital_root(n):
    while n > 9:
        s = 0
        for i in str(n):
            s += int(i)
        n = s
    return n
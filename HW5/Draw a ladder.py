def ladder(n):
    str = ''
    for i in range(n):
        if i != n:
            str = str + '#' * (i + 1) + '\n'
        else:
            str = str + "#" * (i + 1)
    return str
print(ladder(4))

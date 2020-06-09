def ladder(n):
    str = ''
    for i in range(n, 0, -1):
        if i != 1:
            str = str + '#' * i + '\n'
        else:
            str = str + "#" * i
    return str
print(ladder(4))
def ladder(n):
    str = ''
    for i in range(1, n+1):
        if i != n:
            str = str + '#' * i + '\n'
        else:
            str = str + "#" * i
    return str
print(ladder(4))
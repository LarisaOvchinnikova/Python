def ladder(n):
    str = ''
    for i in range(n):
        if i != n:
            str = str + "#" * (n - i) + "\n"
        else:
            str = str + "#" * (n - i)
    return str
x = int(input("Enter number: "))
print(ladder(x))

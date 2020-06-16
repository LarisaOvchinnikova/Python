def matrix(x, y, z):
    t = (z,)
    for i in range(y - 1):
        t = t + (z,)

    res = [t for i in range(x)]
    return res


print(matrix(3, 2, "Hey"))
print(matrix(3, 2, 3.14))
print(matrix(2, 3, "Jack"))
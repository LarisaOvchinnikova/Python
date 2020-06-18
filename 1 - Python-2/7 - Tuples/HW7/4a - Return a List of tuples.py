def matrix(x, y, z):
    return [(z,) * y for i in range(x)]

print(matrix(3, 2, "Hey"))
print(matrix(3, 2, 3.14))
print(matrix(2, 3, "Jack"))
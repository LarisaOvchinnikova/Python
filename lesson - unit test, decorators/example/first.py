def linear(a, b):
    print(f"{a}x + {b}")
    def solve(x):
        return a * x + b
    return solve

import time
def add(x, y = 10):

    return x + y

print("add(1,2) --> ", add(1,2))

# eq1 = linear(2, 3) # 2x + 3
# print(eq1(10))
# print(eq1(11))
# eq2 = linear(3, 1)
# eq3 = linear(5, 4)

# def outer_func(name):
#
#     def inner_func():
#         return f"Hello, {name}"
#     return inner_func
#
# func = outer_func("John")
#
# print(func())
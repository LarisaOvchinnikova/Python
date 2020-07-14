# def func(x=10, y=20): #дефолтные значения без пробелов
#     return x + y
#
# print(func(8, 5)) # 13
# print(func(12))   # 32
# print(func())  # 30

# def func(x, y, z=1):  # все дефолтные справа
#     return (((x, y),) * z)
#
# print(func(1,2,3)) #((1, 2), (1, 2), (1, 2))
# print(func(1,2))  # ((1, 2),)

# def func(y, x=10, z=1):  # все дефолтные справа
#     return (((x, y),) * z)
# print(func(1,2,3)) #((2, 1), (2, 1), (2, 1))
# print(func(1,2))  # ((2, 1),)
# print(func(5, z=5)) # ((10, 5), (10, 5), (10, 5), (10, 5), (10, 5))
#
# print(sorted([1,4,2,6,4])) # reverse by default
# print(sorted([1,4,2,6,4], reverse=True))

def func(x, y):
    print(x, y)

func(y=10, x=0)  #0 10
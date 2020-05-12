try:
    x = int("a")
    print(x)
except ValueError:
    print("Wrong Value")

print("I still work")

try:
    y = 5 / 0
    print(y)
except ZeroDivisionError  :
    print("Zero divizion")

print("I still work")


try:
    print("qwe")
    x = int(6)
    print(x)
    f = open("b.txt")
except NameError as error:
    print(error)
except ValueError as error:
    print(error)
    raise error   # вызвали ошибку чтобы программа прекратилась
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print(error)
finally:
    print("I will print anyway")


print("I still work")





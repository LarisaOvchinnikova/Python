def drunk_say_hello(name):
    name = list(name)
    res = "Hello "
    for i in range(len(name)):
        if i % 2 == 0:
            res = res + name[i].upper()
        else:
            res = res + name[i]
    return ''.join(res)

name = input("Enter your full name: ")
print(drunk_say_hello(name))

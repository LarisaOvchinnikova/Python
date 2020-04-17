def drunk_say_hello(name):
    lst = name.split(' ')
    res = "Hello "
    for i in range(len(lst)):
        if i == 0:
            res = res + f"{lst[i][0].upper() + lst[i][1:].lower()} "
        else:
            res = res + f"{lst[i][0].upper() + lst[i][1:].lower()}"
    return res

name = input("Enter your full name: ")
print(drunk_say_hello(name))

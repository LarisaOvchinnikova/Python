def drunk_say_hello(name):
    lst = name.split(' ')
    res = "Hello "
    for i in range(len(lst)):
        if i == 0:
            for j in range(len(lst[i])):
               if j % 2 == 0:
                   res = res + lst[i][j].upper()
               else:
                   res = res + lst[i][j].lower()
            res = res + " "
        else:
            for j in range(len(lst[i])):
               if j % 2 == 0:
                   res = res + lst[i][j].upper()
               else:
                   res = res + lst[i][j].lower()

    return res

name = input("Enter your full name: ")
print(drunk_say_hello(name))

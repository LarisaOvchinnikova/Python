name = input("Enter name: ")
str = ''
for i, letter in enumerate(name):
    # print(i)  #index of symbol
    if i % 2 == 0:
        str = str + name[i].upper()
    else:
        str = str + name[i]
print(name)
print(str)


name = input("Enter name: ")
arr= []
for i, letter in enumerate(name):
    # print(i)  #index of symbol
    if i % 2 == 0:
        arr.append(name[i].upper())
    else:
        arr.append(name[i])
print(name)
print(arr)
arr = ''.join(arr)
print(arr)



name = input("Enter name: ")
arr= []
for i, letter in enumerate(name):
    print(i)  #index of symbol
    print(letter)
    if i % 2 == 0:
        arr.append(letter.upper())
    else:
        arr.append(letter)
print(name)
print(arr)
arr = ''.join(arr)
print(arr)



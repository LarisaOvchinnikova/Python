name = input("Enter name: ")
name = list(name)
print(name)
for i in range(0,len(name), 2):
    name[i] = name[i].upper()
print(name)
name = ''.join(name)
print(name)
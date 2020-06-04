s = "Hi "
print(s * 3)
print('*' * 5)
num = 6
num = str(num)
print(num)
print("Mary\nhas\na\nlittle\nlamb ")
print("I\'m great")
print("I have a \"good\" weight")
print(len("hello"))
name = "Lara"
print(name[0])
print(name[len(name)-1])
print(name.index("a"))
indexOfR = name.index('r')
print(indexOfR)
# Python console: help(str)  --- get help
print("age="+str(6+4))
name1 = "Bob"
print("His name is %s" %name1)
age = 34
print("His age is %d" %age)
print("%s is %d years old" %(name, age)) # old code
print(f"Hello {name}, you are {age} years old")
print(f"{name} "*5)
print(name[0:2])
print(name[:-1])  # from begin to (last-1)
first = "Alice Moon"
ind = first.index(' ')
print(first[0:ind])
print(first[ind+1:])
print(first[::-1]) # reverse string - from first to last with step - 1
print(first[::2]) # step 2
print(f"{first[0]}.{first[ind+1]}.")
print(f"{first[0:ind]}\n{first[ind+1:]}")

s = "book"
print(s.rjust(10))
print(s.ljust(10))
print(s.center(10,"-"))


s = 'hello'
for i, char in enumerate(s):
    print(i, char)









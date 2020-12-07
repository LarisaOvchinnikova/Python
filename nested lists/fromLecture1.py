population = [
    ["Winterland", "10000"],
    ["Sunrise", "5000"],
    ["Davie", "3000"],
    ["Iron Islands", "4500"]
]
print(population)
print(population[0][0])
print(population[0][0][0])
names = ['Alice', "Bob", "Mark"]
print(names[0][0])

for name in names:
    for letter in name:
        print(letter)
    print('------')


for lst in population:
    for element in lst:
        for letter in element:
            print(letter)
        print(',')
    print('----')

# nested in array - find two elements that sum = n
n = 12
arr = [10, 29, 2, 15]
for el in arr:
    for el1 in arr:
        if el + el1 == n:
            print(el, el1)

print('================')
# find first pair of such elements without duplicates
n = 12
arr = [10, 29, 2, 15, 4, 8]
for el in arr:
    print(el, ':')
    for el1 in arr:
        if el + el1 == n:
            print(el, el1)
            find = True
            break
    if find:
        break
print("===================")
# find all pair of such elements
n = 12
arr = [10, 10, 29, 2, 2, 15, 4, 8]
for el in arr:
   # print(el, ':')
    for el1 in arr:
        if el + el1 == n:
            print(el, el1)
            find = True
            break
print('************************************')
fruits = ['apple', 'banana', 'orange']
for i in fruits:
    print(i)  # 'apple, ...

for i in range(len(fruits)):
    print(i)   # 0,1,2

for i in range(len(fruits)):
    for j in range(1, i + 2):  #apple - 1 times, banana - 2 times, orange - 3
        print(fruits[i])
print('-------------------------------')
table = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1]
]
print(table)
for row in table:
    print(row)
    for cell in row:
        if cell == 0:
            print(cell)  #print 0
print('=====================================')
# print coordinates of this zero:
for x in range(len(table)):
    print(table[x])  # print one row
    for y in range(len(table[x])):
        if table[x][y] == 0:
            print(x, y)

print('===================================')
# print every second letter in UpperCase
name = "John Doe"
name = name.split()
print(name)
newName = ''
for word in name:
    for i, letter in enumerate(word):
     #   print(i, letter)  # J 0, o 1, ...
        if i % 2 == 0:
            newName = newName + letter.upper()
        else:
            newName = newName + letter
    newName += ' '
print(newName[0:-1])


ar = [1,2,3]
print(isinstance(ar, list))

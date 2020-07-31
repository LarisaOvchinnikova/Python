# set is unordered(unindexed), mutable collection of data items
# (items - inmutable - numbers, strings, tuples, boolean)
# set contains only unique values

x = {1, "hello", 3, 5, "world"}
print(len(x))
# to create new empty set, use set() function
# set is unordered(unindexed), mutable collection of data items
# (items - inmutable - numbers, strings, tuples, boolean)
# set contains only unique values

x = set(x)
x = {1, 2, 3, 4, 5}
print(len(x))
print(type(x))

# adding elements  set_name.add() -only one element
x.add(5)
print(x)
x.add(True)
x.add((1,2)) # add tuple
print(x)
x.update((50,30,50)) # добавляет tuple и распаковывает его
print(x)
# массив тоже:
# arr = [1,2,3]
# arr.append(5)
# arr.append([200,300])  # доб.вложенный массив
# arr += [7,8,9]
# print(arr)   # [1, 2, 3, 5, 7, 8, 9]
# arr.extend([-1,-2,-3]) # доб.в массив неск.новых элементов (как сложение  массивов)


x = {1,2,3}
x.add(4)
x.update((5,6,7))
print(x) # {1, 2, 3, 4, 5, 6, 7}

#----------
x = {1,2,3,4,5}
print(1 in x) # True
print(10 in x) # False

# ----
for item in x:
    print(item)


# Deleting elements
# set.remove()  -to remove specified element, error when item doesn't exist in set
# set.discard() - to remove specified element, no error if element doesn't exist
x = {1,2,3}
x.remove(1)
#x.remove(5) #error (no such element)
x.discard(5)
print(x) # {2,3}

# Union (объединение множеств - сетов - общее количество уникалных элементов)
set_A = {1,2,3,4}
set_B = {"a", "b", "c"}
print(set_A | set_B)
print(set_A.union(set_B))

x = {'1','2','3'}
y = {'2','3','4'}
z = x | y
print(z)   # {'1','2','3','4'}
print(" ".join(z))  # соединение в строку сета

# Intersection (пресечение множеств) - то что есть общее в двух сетах
a = {1,2,3,4}
b = {4,5,6,7}
z = a & b # -->{4}
print(z)
z = a.intersection(b)
w = b.intersection(a)
print(z)
print(w)

s = {1,4,2}
r = sorted(s)  # [1, 2, 4]
print(r)

#---
people = {'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
    'paul': ['C++', 'JS', 'Python'],
    'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
    'tim': ['Python', 'Haskell', 'C++', 'JS']}
print(list(people.values()))
p1, p2, p3, p4 = [set(language) for language in list(people.values())]
print(p1 & p2 & p3 & p4)  # {'JS', 'Python'}

# если число элементов неизвестно, нужен цикл
# val1 = p1 & p2
# val2 = val1 & p3
# val3 = val2 & p4

people = [set(language) for language in people.values()]

common = people[0]
for person in people:
    print(common)
    common = common & person

print(common)

# Difference  -- setA - setB те элементы a, которые не входят в b
setA = {1,2,3,4}
setB = {2,4,6,8}
dif = setA - setB
print(dif)   # ---> {1,3}
print(setA.difference(setB)) # --> {1,3}
print(setB.difference(setA)) # --> {6,8}

# какие языки знает Боб, но не знает Пауль
bob = {'JS', 'PHP', 'Python', 'Perl', 'Java'}
paul = {'C++', 'JS', 'Python'}
print(bob - paul) # {'Perl', 'PHP', 'Java'}
print(paul - bob) # {'C++'}

s = {1,2,3}
lst = list(s)
print(lst) # [1, 2, 3]
x = ['1','2','3']
s = set(x)
print(s) # {1, 2, 3}

print(','.join(s))
print(sorted(s, reverse = True)) # ['3', '2', '1']

x1 = 3
x2 = 4
z = set()
z.add(x1)
print(z)

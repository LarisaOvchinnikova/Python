# set is unordered(unindexed), mutable collection of data items
# (items - inmutable - numbers, strings, tuples, boolean)
# set contains only unique values

x = {1, "hello", 3, 5, "world"}
print(len(x))
# to create new empty set, use set() function

x = set()
#length of the set
print(len(x))    # ---> 0

x = {1,1,1,1}
print(x)    # ----> {1}
x = {'hi', 1, 3, (3,6), "hello"}
print(x)
print(len(x))  # -->5
# x = {[1,2,3]}  ---> error, lists, dict can not be element of set

y = [10,20, 30, 40]
x = set(y)
print(y)
print(x)

y = [1, 1, 20, 3, 3, 4, 3] # содержит повторяющиеся элементы
x = set(y)
print(x)  # ---> {1,20,3,4}  - только уникальные элементы

# итерация по set
for i in x:
    print(i)

# сколько различных элементов в массиве
arr = [2,5,2,2,4,5,4]
x = set(arr)
print(x)   # --> {2,4,5}
print(len(x))

# adding elements
# set.add()   to add one element to set
# set.update() to add multiple elements

x = {1,2,3,4}
x.add(5)
print(x)  # -->{1,2,3,4,5}

x.add("hello")
print(x)
x.add(1)
print(x)

x.update("a", "b", "c")
print(x)   # ---> {1, 2, 3, 4, 5, 'hello', 'b', 'a', 'c'}

# Deleting elements
# set.remove()  -to remove specified element, error when item doesn't exist in set
# set.discard() - to remove specified element, no error if element doesn't exist

x.remove("hello")
print(x)
#x.remove('w')  --> error
x.discard("w") # --> no error
print(x)

# Union (объединение множеств - сетов)
set_A = {1,2,3,4}
set_B = {"a", "b", "c"}
print(set_A | set_B)
x = set_A | set_B # ---> объединение выкинет дубликаты
print(x)
x = {1,2,3}
y = {1,2, 6}
z = x | y
print(z)

z = x.union(y)
w = y.union(x)

# Intersection (пресечение множеств)
a = {1,2,3,4}
b = {4,5,6,7}
z = a & b # -->{4}
print(z)
z = a.intersection(b)
w = b.intersection(a)
print(z, w)

# Difference  -- setA - setB те элементы a, которые не входят в b
setA = {1,2,3,4}
setB = {2,4,6,8}
dif = setA - setB
print(dif)   # ---> {1,3}
print(setA.difference(setB)) # --> {1,3}
print(setB.difference(setA)) # --> {6,8}

# Difference between two collections
a = ['a', 'b', 'z', 'd', 'e', 'd']
b = ['a', 'b', 'j', 'j']
setA = set(a)
setB = set(b)
print(setA - setB)
print(setB - setA)


# set from string
s = "hello"
set_s = set(s)
print(set_s)            # {'o', 'e', 'l', 'h'}
print(sorted((set_s)))  # ['e', 'h', 'l', 'o']
# sorted превратидл set в отсортированный массив
x = [1, 2, 3, 4]
print(x[1])

print(x[2:4])
print(x[:3])
print(x[::-1])

x = list(range(0, 10, 1)) # fill array
print(x)

y = list(range(5, 10))
print(y)

z = list(range(20)) #[0,,,,19]
print(z)

w = list(range(10, 0, -1))
print(w)

x = [1, 2, 3, 4, 4, 5]
print(len(x))  #5 - length of array

print(x.index(4))  # 3

print(x.count(4))  # 2

x = [2,5,1,5,7,2]
x.sort()
print(x)
x = ['m', 'a', 'c']
x.sort()  # sort in array
print(x)
x.reverse()
print(x)
l = x.count('c')
print(l)
q = x[::-1]
print(q)

x = [2, 6, 1, 56, 2, 4]
y = sorted(x)  # new sorted array
print(y)
x.sort(reverse=True)  #sort in reverse order
print(x)

lst1 = [1,2,3,4,5]  # ссылочный тип:
lst2 = lst1
print(lst2)
lst2.append(20)
print(lst1)

x = "hello"
print(id(x))
y = x
print(id(y))   # id are the same
y = y +'world'
print(x)
print(y)
print(id(y))  # id changed

x = [1,2,3]
print(id(x))
x.pop()
print(id(x))  # id the same after pop in array because arrays can be changed
x.extend([10, 12, 13])
print(x)

lst1 = [0,0,0]
lst2 = lst1.copy()  # copy of array - new array and we can change lst2 without changing lst1
print(lst1)
print(lst2)
lst2.pop()
print(lst1)
print(lst2)

#copy 2 case
lst1 = [9,9,9]
lst2 = lst1[::]
print(lst1)
print(lst2)
lst2.pop()
print(lst1)
print(lst2)







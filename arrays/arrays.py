lst = []
lst.append(1)  # push
print(lst)
lst.append(2)
print(lst)
lst.insert(0,'a')  # insert in index position
print(lst)
lst.insert(2, 'abc')
print(lst)
x = 'hello'
x = list(x)  # split
print(x)
print(type(x))
lst1 = list("hello")
lst2 = list("world")
lst3 = lst1 + lst2
print(lst3)
x = []
x.extend(lst3)  # concat arrays
print(x)
print("".join(x))  #array to string
print(",".join(x))
print("\n".join(x))

b = [1, 2, 3]
print(b)
b.append(4)
print(b)
b.pop()  # delete last elements
print(b)
b.remove(1)  # delete one element
print(b)
arr = [1, 'hello', [1, 2], 'a', 12, 13]
del arr[0]   #delete one or more elements
print(arr)
del arr[0:2]
print(arr)

if arr.c
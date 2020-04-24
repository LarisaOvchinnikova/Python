arr = ['asff', 'fdlkdld', 's']
list_length = [len(word) for word in arr]
print(list_length)

arr = [1,3,4,5]
newarr = [str(el) for el in arr]
print(newarr)

even = [el for el in arr if el % 2 == 0]
print(even)

arr = ['sfsfj', 'xd', 'kfhfhjhfsh']
arr = [word.rjust(10) for word in arr]  # like arr.map()
print(arr)

fib = [0, 1, 1, 2, 3, 5, 8]
fib = ", ".join([str(num) for num in fib])
print(fib)

x = [number for number in range(10) if number % 3 == 0]
print(x)  # create array [0,3,6,9]

x = ["Even" if n % 2 == 0 else "Odd" for n in range(10)]
print(x)

# [-1, 2, -3, 4, -5...]
x = [number if number % 2 == 0 else -number for number in range(10)]
print(x)

x = ["hello", "world", "sky", "blue"]
x = [word.capitalize() for word in x]
print(x)

q = ['a', 'abc', 'aa', 'qwerty']
z = [len(word) for word in q]
print(z)



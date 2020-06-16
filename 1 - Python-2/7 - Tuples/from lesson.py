# четные буквы-заглавные, нечетные - строчные
text = list("Hello, how are you?")

new = []
for i in range(len(text)):
    if i % 2 == 0:
        new.append(text[i].upper())
    else:
        new.append(text[i].lower())
print("".join(new)) # HeLlO, hOw aRe yOu?

# с использованием list comprehension
# вспомним if-else - переменная greet получает разные значения
#  в зависимости от условия
name = "John"
if name[0].isupper():
    greet = "good day"
else:
    greet = "Howdy"

# тернарный оператор при записи list comprehension
# value_if true if condition else value_if_false

num = 5
status = "Positive" if num > 0 else "Negative"
print(status)

text = list("Hello, how are you?")
new = [char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text)]

print(new)

# удвоить четные элементы, утроить нечетные для всех полож.элементов массива
arr = [1, -3, 9, 4, -4]
lst = [el * 2 if el % 2 == 0 else el * 3 for el in arr if el > 0]

# есть текст из слов. Перевернуть все слова их текста, если их длина >= 5,
# остальные не изменять
text = "Stop spinning my words"
new = [word if len(word) < 5 else word[::-1] for word in text.split()]
print(" ".join(new))

# -------------------------------------------------------------------------
# Tuples - неизменяемые списки записываются в круглых скобках
my_tuple = (10, 20, 30)
print(my_tuple) # (10, 20, 30)
print(type(my_tuple)) # <class 'tuple'>

print(my_tuple[0])   # 10
print(my_tuple[1:])  # (20, 30)

x = (10, 20)
print (x)

# или возможна запись
x = 10, 20
print(x)  # (10, 20)

x = (10, )  # tuple from 1 element
print(x)
#или:
x = 10,   # tuple
# изменять нельзя, поэтому нет методов append, remove и др
# tuples можно складывать
x = (1, 2, 3)
y = (40,)
z = x + y
print(z)  # (1, 2, 3, 40)

w = (10, 0 ) + x[1:]
print(w)  # (10, 0, 2, 3)

# разница между списками и таплес
# списка мутабельны. таплес иммутабельны
# lists are homogeneous sequences. tuples heterogenius data structures
people = ["John", 15, "market street", "Sarah", 27, "some street"]
person = ("John", 15, "market street")

p1 = (10, 20) # coordinates of point - 2 numbers x and y
p2 = (-5, 30)
p3 = (40, 5)

points = [p1, p2, p3] #  массив точек
# list to tuple

print(list(p1))  # [10, 20]
print(tuple(points)) #((10, 20), (-5, 30), (40, 5))

# -----
def func(x, y):
    return x, y      #  (x, y) --> (9, 3) возвращает tuple
print(func(9,3))

text = "hello"
for i in enumerate(text):
    print(i)   # i--> tuples, поэтому мы пишем i, char in enumerate(text)
    # (0, 'h')
    # (1, 'e')
    # (2, 'l')
    # (3, 'l')
    # (4, 'o')


# -----
time = "19:30".split(":")
print(time)
# hours = time[0]
# minutes = time[1]
hours, minutes = time  # количество элементов слева и справа должно совпадать
print(hours, minutes)  # 19  30

# ---
x, y = 12, 23
print(x, y)


hours, minutes = "12:20".split(":")
print(hours, minutes)  # 12   20

# начальное присаивание
count, sum = 0, 0
print(count, sum)

# менять значения переменных
x = 10
y = 20
x, y = y, x
print(x, y)  # 20 10

# -------------
# name = input("Enter full name").split()
# first = name[0]
# last = name[1]
# or:
name = input("Enter full name").split()
first, last = name
print(first, last)

# ----
first, last = input("Enter full name").split()
print(first, last)
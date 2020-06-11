x = []
y = [1,2,3]
z = list(range(10))
s = list("hello")
# добавление в массив
# x.append(object)
# x.insert(index, object) - insert object before index
# [1,2,3] + [4,5,6] = [1,2,3,4,5,6]
y.append(100)
print(y)  # [1, 2, 3, 100]
y.insert(2,300)
print(y)  # [1, 2, 300, 3, 100]
lst1 = y + s
print(lst1) # [1, 2, 300, 3, 100, 'h', 'e', 'l', 'l', 'o']
# append ничего не возвращает
z = y.append(1)
print(z) # None
lst1.insert(-1, 1000) #добавляет 1000 перед последним элементом
print(lst1)

for i in range(5,10):  #добавляет в конец числа от 5 до 9
    lst1.append(i)
print(lst1)

# соединять число и массив нельзя, толко массив с массивом:
lst1 = [0,1,2]
lst2 = [3]
lst3 = lst1 + lst2 #[0,1,2,3]

# удаление элементов
# x.remove(value) убирает один элемент слева

lst = [0, 1, 2, 1, 0, 1]
lst.remove(1)
print(lst)   # [0, 2, 1, 0, 1]
while True:
    if 1 in lst:
        lst.remove(1)
    else:
        break
print(lst)  # [0, 2, 0]


# x.pop(index) - remove element at given index

lst = [0,1,2,1,5]
lst.pop(-2) # удалили второй элемент с конца
print(lst) #[0, 1, 2, 5]
lst.pop() # если не указывать индекс, то удаляется 1 элемент с конца
print(lst) #[0,1,2]

# x.count(el) - количество элементов в массиве
lst = [1,2,3,2]
s = lst.count(2)
print(s)  # 2

# как удалить все 1 в массиве:
for i in range(lst.count(1)):
    lst.remove(1)

# del x[a:b] - deletes all the elements from index a to b
lst = [0,1,1,1,1,0]
del lst[1:4]
print(lst)  #[0,1,0]

# Range function
print(range(10))  # range(0, 10) - объект в Питоне
for i in range(10):
    print(i)   # печатает числа из range

lst = list(range(10))
print(lst)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# то же самое можно сделать по-другому:
lst = []
for i in range(10):
    lst.append(i)
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Indexes and slicing
# x[0], x[-1], x[2:7]

# Task 1: ввести текст, найти среднюю длину слов и результат
# округлить до сотых
# Найти самое длинное и самое короткое слово
s = "i like summer"
words = s.split() # разбивает строку на массив слов по пробелам
print(words) # ['i', 'like', 'summer']
total = 0
for word in words:
    print(word)
    total += len(word)

average_length = round(total / len(words), 2)
print(average_length)

len_lst = []   # массив длин слов
for word in words:
    len_lst.append(len(word))
print(len_lst)

# print (sum(len_lst)) # второй способ найти сумму длин слов
minimum = min(len_lst)
for word in words:
    if len(word) == minimum:
        print(f"The shotrtest word is {word}")

maximum = max(len_lst)
for word in words:
    if len(word) == maximum:
        print(f"The longest word is {word}")

#как работать с длинной строкой
# print("kjkdjk\
# jfjgj")
#
# x = ["hello",
#      "how",
#      "are",
#      "you"]
# print(x)
#
# # элемент массива -  переменная?
# y = "Hello"
# x = "Hi"
# lst = [x, y]
# print(lst)  # ['Hi', 'Hello']

#Task
print('-----------------')
text = "Shine on your crazy diamond!".split()
shortest = None
shortest_length = 0

for word in text:
    if shortest == None:
        shortest = word
        shortest_length = len(word)
    else:
        if shortest_length > len(word):
            shortest = word
            shortest_length = len(word)
print(shortest_length)
print(shortest)

s = list("hello")
print(s)  # ['h', 'e', 'l', 'l', 'o']
s = ['h', 'e', 'l', 'l', 'o']
word = "".join(s)
print(word)

st = "how are you"
arr = st.split(" ")
print(arr)
arr[1] = arr[1].upper()
print(arr)
res = " ".join(arr)
print(res)
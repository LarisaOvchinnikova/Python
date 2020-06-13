# в столбик слова предложения
s = "Shine on your crazy diamond"
arr = s.split()
arr = '\n'.join([el.rjust(10) for el in arr])
print(arr)

# сортировка
names = ["Bob", "Alice", "Sara", "Jim"]
new_names = sorted(names)
print(new_names)

nums = [3,1,5,3,8,4]
new_nums = sorted(nums)    # создает новый отсортированный массив
print(nums) # [3, 1, 5, 3, 8, 4]
print(new_nums) # [1, 3, 3, 4, 5, 8]

nums = [4, 2, 5]
nums.sort()  # меняет сам массив, но ничего не возвращает
print(nums)  #[2, 4, 5]

# Получить 2 самых маленьких числа массива
arr = [4,6,19,9, 4, 7, 0, 67, -2]
def get_2_min(numbers):
    nums = sorted(numbers)
    return nums[0:2]

print(get_2_min(arr))


# Пример убрать из массива четные числа отсортированные
def func(numbers):
    new = []
    for num in numbers:
        if num % 2 == 0:
            new.append(num)
    #return sorted(new)              # [-2, 0, 4, 4, 6]
    return sorted(new, reverse=True) # [6, 4, 4, 0, -2]
print(func(arr))

# List are mutable data structure
names = ["Bob", "Alice", "Sara", "Jim"]
names[0] = "Artem"
print(names)

#strings ate not mutable
# s = "Lola"
# s[0] = "l"  #Error

name = "Alice"
name = name + "!"
print(name) # изменилась!??

print("Hello world") # строка в памяти не сохраняется
x = "Hello world"  # x - указатель на область памяти
print(x)
print(id(x))  # 1623448
x = "Hi"
print(x)
print(id(x))  # 8086560 поменялась ячейка памяти
# удалилась старая строка, получился новый объект

# то же самое с числами - not mutable
n = 9
print(id(n))
n = 10
print(id(n))  # разные id

num1 = 10
num2 = 10
print (num1, num2)  # - ссылаются на один объект
print(id(num1)) # 1450702912
print(id(num2)) # 1450702912

num2 += 5
print(id(num1)) # 1450702912
print(id(num2)) # 1450702992 изменилась

# List are mutable
arr = [1,2,3]
print(id(arr)) #2629960
arr[0] = 10
print(id(arr)) #2629960 - не изменилось

# создадим копию массива
arr = [5,4,3,2,1]
arr1 = arr
print(arr)
print(arr1)
arr1[0] = "a"
print(arr) # тоже изменился , так как находится по тому же самому ID
print(arr1)
arr.remove(1)
print(arr)
print(arr1)  # элемент удвлился из обоих массивов,
# так как это ссылки на один и тот же объект

arr1 = [1,2,3,4,5]
arr2 = arr1.copy()
# это два разных объекта

print(arr1, arr2) # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]
arr1[0] = 0
print(arr1, arr2) # [0, 2, 3, 4, 5] [1, 2, 3, 4, 5]

arr = [1,2,3,4,5]
arr1 = arr[:]
# тоже создано два разных объекта (используется slice)

# удалить из массива все слова длиной больше 5
# в примере ниже
# не работает remove остается ['Cat', 'Dog', 'Zebra', 'Bat']
# так как приудалении смешаются элементы влево и пропускаем элементы

def filter_vowel(lst):
    for word in lst:
        if len(word) >= 5:
            lst.remove(word)

    return lst

items = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
filtered_list = filter_vowel(items)
print(filtered_list)

# поэтому в цикле поставим интерирование по копии

def filter_vowel(words):
    for word in words.copy(): # проходим по копии, а удаляем в оригинале (в другом массиве
        if len(word) >= 5:
            words.remove(word)
    return words

words = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']

filtered_list = filter_vowel(words)
print(filtered_list)   # ['Cat', 'Dog', 'Bat']

# List Comprehension - a new short-hand
# way of building a list from a collection of values or a sequence


# Пример - создать массив из этих имен, сделав буквы заглавнми
# можно сдеалть цикл с добавлением в новый массив:
names = ["alice", 'anna', 'bob', " sasha"]
new = []
for name in names:
    new.append(name.title())
print(new)

# 2 способ с list comprehension
# (это новый способ генерировать списки)
# т.е замена дабавления измененного элемента в новый список
names = ["alice", 'anna', 'bob', " sasha"]
text = [name for name in names]
print(text) #  получился такой же:['alice', 'anna', 'bob', ' sasha']

new_text = [name.title() for name in names]
print(new_text) # ['Alice', 'Anna', 'Bob', ' Sasha']
new = [name[::-1] for name in names]
print(new) # ['ecila', 'anna', 'bob', 'ahsas ']


# Пример. Есть список из чисел, сделать список из строк
x = list(range(10))
print(x)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [str(el) for el in x] # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(x)

# Оставить в списке только строки длиной меньше 5
arr = ['Alice', 'Anna', 'Bob', ' Sasha']
arr = [el for el in arr if len(el) < 5]
print(arr)  # ['Anna', 'Bob']

# оставить слова начинающиеся с буквы
words = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
new = [word for word in words if word[0].lower() in "aeuio"]
print(new) # ['Apricot', 'Ocelot', 'Orange']

# оставить только четные значения
nums = [1,4,2,7,8,9,10]
nums = [el for el in nums if el % 2 == 0]
print(nums)


# сумма положительных чисел массива
arr = [2, -5, 8, 0, -4]
s = sum([el for el in arr if el > 0])
print(s)  # 10
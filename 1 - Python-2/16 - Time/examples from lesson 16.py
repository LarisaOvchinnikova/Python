import time

def sum_numbers(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return total  # O(n) - сложность алгоритма



# start = time.time()
# #time.sleep(1) # 1 sec
# for i in range(100):
#     sum_numbers(1000)
# end = time.time()
# print("Time elapsed", end - start)

# for i in range(5):
#     print(i)
#     time.sleep(0.5)

# start = time.time()
# for i in range(100):
#     sum_numbers(1000)
# end = time.time()
# print("Time elapsed for 1000:", end - start)
#
#
# start = time.time()
# for i in range(100):
#     sum_numbers(10000)
# end = time.time()
# print("Time elapsed for 10000:", end - start)


# def sum_numbers_2(n):
#     return n * (n + 1) /2
# # сложность алгоритма O(1) - константное время(не зависит от n)
#
#
# start = time.time()
# for i in range(100):
#     sum_numbers_2(1000)
# end = time.time()
# print("Time elapsed for 1000:", end - start)
#
# start = time.time()
# for i in range(100):
#     sum_numbers_2(1000000)
# end = time.time()
# print("Time elapsed for 1000000:", end - start)

# ----
# def func(n):
#     for i in range(n):
#         for j in range(n):
#             q = j
# O(n**2)  сложность n в квадрате
#т.е для n = 100 будет 10000 операций


# start = time.time()
# func(10)
# end = time.time()
# print("Time elapsed for 10:", end - start)
#
# start = time.time()
# func(100)
# end = time.time()
# print("Time elapsed for 100:", end - start)
#
# start = time.time()
# func(1000)
# end = time.time()
# print("Time elapsed for 1000:", end - start)
#
# start = time.time()
# func(10000)
# end = time.time()
# print("Time elapsed for 10000:", end - start)

# ----------------------------------------------------
# как сложность алгоритма связана со списками, сетами  и словарями?
# итерация по списку O(n) n - длина списка
# удаление элемента с конца списка - константное время
# удаление элемента в середине - занимает больше времени, так как
# элементы надо переместить к началу

# напечатать элемент массива print(a[2])  - константное время
# присваивание элементу нового значения a[2] = "q" - константное время

# если надо найти букву в массиве - есть ли в массиве буква о
# для этого надо итерация по массиву
# т.е. для выполнения "o" in arr надо O(n) времени

# для удаления элемента arr.remove("у") тоже итерация

# for word in dict:
#     if word in text:
#         print(word) # сложность  O(m*n) m-длина словаря n - длина текста

# ------------------------------------------------
# для ускорения алгоритма используем сеты
#  элементы сета не имеют индексов
# элементы находят не по индексам а по значениям
# это делает функция hash
print(hash("Hello"))
print(hash("Hello"))  # одинаковое значение при одном запуске
# при следующем запуске - другое значение

print(hash("q"))
print(hash(5)) # никальное значение для каждой величины

set1 = {"hello"}
print(set1)
print(hash("hello"))

#можно проверить есть ли в сете какое-то значение с таким хэшем

# word_dict = set(word_dict)
# new_text = []
# for word in text:
#     if word in word_dict:
#         new_text.append(word) # гораздо быстрее, так как списко превратили в сет
        
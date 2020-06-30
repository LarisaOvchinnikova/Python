file_handler = open("most_common_words.txt")
print(file_handler)
# <_io.TextIOWrapper name='most_common_words.txt' mode='r' encoding='cp1251'>

# читаем файл по строкам 1 способ
for line in file_handler:
    print(line, end='')

# чтобы убрать пробелы и пустые строки
for line in file_handler:
    line = line.rstrip() #удаление пробелов и переносов строк \n
    if len(line) > 10:
        print(line)  # остаются только длинные слова

file_handler.close()    # закрываем файл

# x = "hello\nworld"
# print(repr(x)) #'hello\nworld'
# a = "hello\n   "
# a = a.rstrip()
# print(a)
# print(repr(a))  #'hello'


file_handler1 = open("text.txt")
text = file_handler1.read()  # все одной строкой через \n
text = text.split() # разбиваем на строки и одновременно удаляем \n
print(repr(text))

for word in text:
    print(word)

# ----

file_handler1 = open("text.txt")
text = file_handler1.readlines()  # возвращает массив из строк в конце которых \n
text = [line.rstrip() for line in text] # удаляем переносы строк в каждом элементе
print(repr(text))

# -----
file_handler1 = open("text.txt")
text = file_handler1.readlines() # текст прочитан, курсор в конце

file_handler1.seek(0) # перемещает курсор в файле в начало

# ====
file_handler = open("text.txt")
line_list = []
for line in file_handler:
    line_list.append(line)
    if line == "monkeys\n":
        break
print(line_list)
file_handler.seek(0)
for line in file_handler:
    line_list.append(line)

print(line_list)

# -----
file_handler = open("text.txt", "w")

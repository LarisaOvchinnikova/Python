f = open("my_text.txt", "w")
f.write("Hello world!\n")  # весь старый текст сотрется и перезапишется
f.close()

for i in range(10):
    f = open("my_text.txt", "a")  # к тексту 10 раз добавим слова
    f.write("Hello\n")
    f.close()

f = open("my_text.txt")  # -если без параметра, значит только для чтения
# text = f.read()  # получаем содержимое файла в виде строки
# print(text)

for line in f:
    print(line)   # так как после каждой строки записан \n происходит переход
    # на новую строку  и каждая строка оператором печатается еще с новой строки

for i in range(5):
    print("hello", end=";")  #  печатает в одну строку без перехода на нов.строку
for i in range(5):
    print("hello", end="\n")  # каждая строка с новой строки

# -----
f = open("my_text.txt")
#text_str = f.read()         # содержимое файла в виде строки
text_list = f.readlines()   # получен массив из строк файла
#print(text_str)
f.close()
print(text_list)
for lst in text_list:
    print(lst, end = "")

# -------------------
f = open("my_text.txt")
text_str = f.read()
print(text_str.split())
f.close()
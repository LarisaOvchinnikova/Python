file_handler = open("text.txt", "w")

file_handler.write("Hello from file writer")  # переписывает все содержимое файла

# если файла для записи нет, то он будет создан

file_handler = open("new_test.txt", "w")
file_handler.write("Hello from lesson")  # создает файл и записывает в него

# -----
file_name = input("Enter file name: ")
file_handler = open(file_name, "w")
file_handler.write("Hello from Script!")
for name in "Hello from Script".split():
    file_handler = open(name, "w")   # создаются файлы с именами слов строки
    file_handler.write("hello!! ")
    file_handler.close()


# ----
file = open("text.txt", "a")
file.write("Hello from\n")
file.write("hello again\n")
file.close()
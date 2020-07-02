import os
# os.mkdir("Harry Potter Book1") # Создана папка
path = os.path.join(os.getcwd(), "Harry Potter Book1")

print(path)
book = open("harry potter and the sorcerer's stone.txt", encoding="utf-8-sig")

text = book.readlines()[3:]
#print(text[:3]) # первые три строки

buffer = []
chap_count = 1
for line in text:
    if line.startswith("CHAPTER") and not line.startswith("CHAPTER ONE"):
        file_name = f"{chap_count}. {buffer[3].strip()}"
        path = os.path.join(os.getcwd(), "Harry Potter Book1", file_name)
        #print(path)
        new_file = open(path, "w")
        new_file.write("".join(buffer))
        new_file.close()
        buffer = []
        chap_count += 1

    buffer.append(line)
file_name = f"{chap_count}. {buffer[3].strip()}"
path = os.path.join(os.getcwd(), "Harry Potter Book1", file_name)
#print(path)
new_file = open(path, "w")
new_file.write("".join(buffer))
new_file.close()
buffer = []
chap_count += 1
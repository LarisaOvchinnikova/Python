import os

os.mkdir("Harry Potter Book 1")  # create new directory

book = open("harry potter and the sorcerer's stone.txt")
text = book.readlines()[3:]  # skip first 3 empty lines

buffer = []
chap_count = 1

for line in text:
    if line.startswith("CHAPTER") and not line.startswith("CHAPTER ONE"):
        file_name = f"{chap_count}. {buffer[3].strip()}"  # buffer[3] it's the name of the chapter
        path = os.path.join(os.getcwd(), "Harry Potter Book 1", file_name)

        new_file = open(path, "w")
        new_file.write("".join(buffer))
        new_file.close()

        buffer = []
        chap_count += 1

    buffer.append(line)  # add line to buffer

file_name = f"{chap_count}. {buffer[3].strip()}"
path = os.path.join(os.getcwd(), "Harry Potter Book 1", file_name)
new_file = open(path, "w")
new_file.write("".join(buffer))
new_file.close()
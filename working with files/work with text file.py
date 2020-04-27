f = open("test.txt")    # open file
print(f.read())         # read file
x = f.read()         # this a string
print(x)
print(type(x))
f.close()    # close file
# -----------------------
f = open("hello.txt")
x = f.read()
print(x)
f.close()
# --------------------
f = open("test.txt", "w") # mode  for writing просто переписывает файл,
# удаляет все что было раньше
x = f.write("new word that add in program")
f.close()
# ------------------------------
f = open("test.txt", "a") # mode adding to file
f.write("hello!!!!")    # add this text to file
f.close()
# --------------------
# если файл не создан, можно его создать
f = open("new.txt", "w")
f.write("This file I create in program\n")
f.write("new string")
f.close()
f = open("new.txt", "a")
f.write('\nho-ho\n')
f.close()

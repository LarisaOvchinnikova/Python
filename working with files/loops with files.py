for i in range(10):
    f = open(f"f{i}.txt", "w")  # создали 10 файлов
    f.close()

for i in range(10):
    f = open(f"f{i}.txt", "a")
    f.write(f"Hello file number {i}\n")
    f.write(f"{i} * {i} = {i*i}")

    f.close()



f = open("mbox.txt")
emails = f.readlines()
f.close()
arr = []
for lines in emails:
    if lines.startswith("From"):
        index = lines.index(" ")
        lines = lines[index + 1:].split()
        arr.append(lines[0])
print(len(arr))
print(arr)
x = set(arr)
print(len(x))
print(x)

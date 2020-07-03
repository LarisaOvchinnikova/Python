f = open("mbox.txt")
emails = f.readlines()
f.close()
arr = []
for lines in emails:
    if lines.startswith("From:"):
        print(lines)
        lines = lines.split()
        print(lines)
        arr.append(lines[:2])
print(len(arr))
print(arr)



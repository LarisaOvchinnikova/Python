f = open("mbox.txt")
emails = f.readlines()
f.close()
arr = []
for lines in emails:
    if lines.startswith("From:"):
        lines = lines.split()
        arr.append(" ".join(lines[:2]))

print(arr)



f = open("mbox.txt", "r")
file = f.readlines()
f.close()
emails = []
for line in file:
    if line.startswith("From:"):
        new_email = line.split()[1] #убирает все пробелы и переносы строк
        if new_email not in emails:
            emails.append(new_email)

print(emails)

for get_email in emails:
    print(get_email)


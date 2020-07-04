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



file_to_write = open("only_emails.txt", "w")
# for get_email in emails:
#     file_to_write.write(get_email) # записали в файл все одной строкой

#file_to_write.write("\n".join(emails)) # 1 способ

for new in emails:
    file_to_write.write(new+'\n')

file_to_write.close()
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        year = 365
    else:
        year = 366
else:
    year = 365

print("Количество дней в году:", year)
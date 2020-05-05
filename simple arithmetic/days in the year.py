year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        days = 365
    else:
        days = 366
else:
    days = 365

print("Количество дней в году:", days)
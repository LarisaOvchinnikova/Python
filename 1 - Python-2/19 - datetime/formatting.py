from datetime import date, timedelta, datetime

day = date.today()

print(day)  # 2020-07-13
# дату в строку d - day b -month Y - year
print(day.strftime("%d %b, %Y")) # 14 Jul, 2020
print(day.strftime("%A, %d %B, %Y")) # Tuesday, 14 July, 2020
print(day.strftime("%A, %d of %B, %y")) # Tuesday, 14 of July, 20

day = datetime.today()
print(day.strftime("%A, %d %b, %Y. Current time is - %H:%M"))


#из строки во время
day1 = "2020-07-14"
day2 = datetime.strptime(day1, "%Y-%m-%d")
print(day2) #
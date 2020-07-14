from datetime import datetime, date, timedelta

day = date.today()  # today() - это метод класса
print(day) # 2020-07-13
print(type(day))
print(isinstance(day, date))  #True - day is type of date

print(day.year)  #2020   - это атрибуты класса
print(day.month)  # 7
print(day.day)  # 13

new_year = date(2021, 1, 1)
print(new_year) #2021-01-01
print(new_year.weekday()) #4 (день недели начиная с 0 - monday)
print(dir(date)) # все методы класса

day = datetime.today()
print(day) #2020-07-13 23:25:25.825200
print(day.hour)  # 23
print(day.time()) # 23:26:20.438200
print(dir(datetime))


if date.today() == new_year:
    print("Happy New Year")
else:
    print("Good day")


day1 = datetime.today()
day2 = date.today()
print(day1 == day2) # False - это разные типы и значения

# сколько дней до нового года
day = datetime.today()
print(day)  # 2020-07-13 23:34:18.453200
diff = timedelta(days=1)
print(diff) # 1 day, 0:00:00

print(day + diff) # 2020-07-14 23:34:18.453200
diff = timedelta(days=5, hours=4)
print(diff) # 5 days, 4:00:00

print(diff.seconds) #14400

diff = timedelta(weeks=2)
print(diff) # 14 days, 0:00:00

print(diff.seconds)
print(diff.total_seconds()) # 1209600.0

print(day - diff) # 2020-06-29 23:40:18.545200 -дата де недели назад

day = date.today()
diff = timedelta(days=1)

new_year = date(2021, 1, 1)
old_year = date(2020, 1, 1)
if day == new_year:
    print("Happy New Year")
else:
    print(f"It's {(new_year-day).days} days until the new Year")
    print(f"It's {(day - old_year).days} days past the last new Year")

#
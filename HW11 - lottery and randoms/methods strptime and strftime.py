from datetime import datetime, date, timedelta

today = datetime.today()
print(str(today))  # 2020-05-10 20:46:17.842205
print(type(str(today))) # <class 'str'>

# strftime - переводим время из формата datetime в строку
today = today.strftime("%B %d, %Y")  # %B - полный месяц, % d - номер дня, %Y год
print(today) # "May 10, 2020

#  создадим другое время
d = datetime(2020, 6, 12)
d = d.strftime("%B %d, %Y")
print(d) # June 12, 2020

#  создадим другое время
d = datetime(2020, 9, 12)
d = d.strftime("%b %d, %Y")  # %b - сокращенное название месяца Sep
print(d) # Sep 12, 2020

d = datetime(2020, 9, 12)
d = d.strftime("Today is %d %b, %Y")  # %b - сокращенное название месяца Sep
print(d) # Today is 12 Sep, 2020

# strptime(строка, формат) ---> перевод строки в datetime
d = datetime(2020, 9, 12)
d = d.strftime("%d %b, %Y")
print(d)   # "12 Sep, 2020"
# print(type(d))  # str
print(datetime.strptime(d, "%d %b, %Y"))  # 2020-09-12 00:00:00

day = datetime.strptime(d, "%d %b, %Y")
print(type(day))  # <class 'datetime.datetime'>

day = datetime.strptime(d, "%d %b, %Y").date()
print(type(day))  # <class 'datetime.date'>
print(day)  # 2020-09-12


today = datetime(2020, 9, 12)
print(today) # 2020-09-12 00:00:00
print(datetime.today()) # 2020-05-10 21:21:51.161005


day = date(2020, 5, 10)
print(day) # 2020-05-10
print(day.weekday())  # 6 (воскресенье)


# переведем day в строку
day = day.strftime("%A %d %b, %Y")   # Sunday 10 May, 2020
print(day)
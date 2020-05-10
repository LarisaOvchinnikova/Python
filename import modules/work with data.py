from datetime import datetime, date, timedelta
#import datetime

print(datetime.today())
today = datetime.today()
print(str(today))  # 2020-05-09 18:10:23.582502
print(today.year)
print(today.day)
print(today.month)


today = date.today()  # 2020-05-09
print("-------------------")
print(today)
print(today.month)
new_year = date(2021,1,1) # задаем свою дату
print(new_year)  # 2021-01-01
print(new_year - today)   #сколько дней до нового года
print(type (new_year-today))  # <class 'datetime.timedelta'>
print((new_year - today).days)  # дней до нового года

# можно задавать самим разницу во времени
print("====================")
diff = timedelta(days = 4)
print(today + diff)

diff = timedelta(days = 14, hours = 20, seconds = 30)
print(today + diff)

today = date.today()
if today == new_year:
    print("Happy New Year")
else:
    print(f"It's still {(new_year - today).days} days until New Year")

wait_time = new_year - today #тип timedelta
print(wait_time.days)

#можно запомнить дату начала теста(игры, написания кода)
# и дату окончания и отняв первую дату от второй даты
# можно получить время написания кода, прохождения теста и т.п.

start = datetime.today() # в начале программы

end = datetime.today() #  в конце программы

diff = (end - start).seconds
print(diff)

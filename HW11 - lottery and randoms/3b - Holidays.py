from datetime import datetime, date, timedelta
# скачали из интернета строку
dates = """
New Year's Day                   Wed, Jan 1, 2020  
Martin Luther King Jr. Day       Mon, Jan 20, 2020  
Memorial Day                     Mon, May 25, 2020  
Independence Day                 Fri, Jul 3, 2020  
Labor Day                        Mon, Sep 7, 2020   
Veterans Day                     Wed, Nov 11, 2020   
Thanksgiving                     Thu, Nov 26, 2020   
Christmas Day                    Fri, Dec 25, 2020   
"""
# делаем из этой строки словарь
# print(dates.split("  "))


dates = [name.strip() for name in dates.split("  ") if name.strip() != ""]
print(dates)

# протестируем как все работает:
# переведем строку 'Wed, Jan 1, 2020' в тип date  ---> 2020-01-01
print(datetime.strptime('Wed, Jan 1, 2020', "%a, %b %d, %Y").date())

#holidays = {datetime.strptime(dates[i+1], "%a, %b %d, %Y").date(): dates[i] for i in range(0, len(dates), 2)}
#print(holidays)

# то же с помощью цикла
holidays = {}
for i in range(0, len(dates), 2):
    holidays[datetime.strptime(dates[i+1], "%a, %b %d, %Y").date()] = dates[i]
   # holidays[dates[i+1]] = dates[i]
print(holidays)

# решаем задачу - какой ближайший праздник
today = date.today()  # для сегодняшней даты
print(today)  # 2020-05-10
# или пишем любую датy:
# today = date(2020, 1, 1)
# или для даты, введенной пользователем:
# today = input("Enter date in format: yy mm dd ").split()
# today = date(int(today[0]), int(today[1]), int(today[2]))
# а можно и так:
# today = input("Enter date in format: yy mm dd ")
# today = datetime.strptime(today, "%Y %B %d").date()
# print(today)

if today in holidays:
    print(f"Happy {holidays[today]}!")
else:
   # time = min([date - today for date in holidays.keys() if date - today > timedelta(0)])
   # print(f"Good news! There are {time.days} until the {holidays[today + time]}")
   # с помощью цикла:
   diff_in_time = []
   for date in holidays.keys():
       if date - today > timedelta(0):
            diff_in_time.append(date - today)
   print(diff_in_time)
   print(min(diff_in_time))
   print(min(diff_in_time).days)
   time =min(diff_in_time)
   print(f"Good news! There are {time.days} until the {holidays[today + time]}")
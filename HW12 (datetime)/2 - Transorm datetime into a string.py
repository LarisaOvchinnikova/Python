from datetime import datetime
# strftime - переводим время из формата datetime в строку


today = datetime.today()
print(today)
year = today.strftime("%Y")
print(f"year: {year}")
month = today.strftime("%m")
print(f"month: {month}")
day = today.strftime("%d")
print(f"day: {day}")
time = today.strftime("%I:%M:%S")  #12-hour clock
print(f"time in 12-hour clock: {time}")
time = today.strftime("%H:%M:%S")  #12-hour clock
print(f"time in 24-hour clock: {time}")
date_and_time = today.strftime("%m/%d/%Y, %H:%M:%S")
print(f"date and time: {date_and_time}")
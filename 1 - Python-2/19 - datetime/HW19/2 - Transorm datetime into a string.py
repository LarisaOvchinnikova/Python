from datetime import datetime

today = datetime.today()
print(today)  # 2020-07-14 15:22:23.913000
year = today.strftime("%Y")
print(f"year: \"{year}\"")
month = today.strftime("%m")
print(f"month: \"{month}\"")
day = today.strftime("%d")
print(f"day: \"{day}\"")
time = today.strftime("%I:%M:%S %p")  #12-hour clock
print(f"time in 12-hour clock: \"{time}\"")
time = today.strftime("%H:%M:%S")  #24-hour clock
print(f"time in 24-hour clock: \"{time}\"")
date_and_time = today.strftime("%m/%d/%Y, %H:%M:%S")
print(f"date and time: \"{date_and_time}\"")
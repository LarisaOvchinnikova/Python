# Print a full weekday's name of the first day of every month
from datetime import datetime, date, timedelta

start = date(2020, 1, 1)
end = date(2020, 12, 31)

i = start
while i <= end:
    first_day = i.strftime("%d")
    if first_day == "01":
        print(i.strftime("%B %d: %A"))
    i = i + timedelta(days = 1)

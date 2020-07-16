# Print a full weekday's name of the first day of every month
from datetime import date
month = 1
first_weekday = [date(2020, month, 1) for month in range(1,13)]

for day in first_weekday:
    print(day.strftime("%B %d: %A"))


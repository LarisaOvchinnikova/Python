from datetime import datetime, date, timedelta
# Print a list of dates of every Sunday in 2020
# You can use .weekday() method
start = date(2020, 1, 1)
end = date(2020, 12, 31)
print(start, end)

lst_of_Sundays = []
i = start
while i <= end:
    # print(i)
    # print(i.weekday())
    if (i.weekday() == 6):
        date = i.strftime("%m/%d/%Y")
        lst_of_Sundays.append(date)
    i = i + timedelta(days = 1)
print(lst_of_Sundays)
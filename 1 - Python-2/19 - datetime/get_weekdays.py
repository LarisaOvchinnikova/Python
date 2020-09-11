from datetime import date, timedelta

start = date(2020, 1, 1)
end = date(2021, 1, 1)

# sundays = []
#
# for day in range(366):
#     #print(timedelta(day))
#     next_day = start + timedelta(day)
# #    if next_day.weekday() == 6: # sunday
#     if next_day.weekday() in [5,6]: # saturday, sunday
#         sundays.append(next_day)
#         print(next_day)


# Extend weekends
# https://www.codewars.com/kata/5be7f613f59e0355ee00000f/train/python
start = date(2016, 1, 1)
end = date(2020, 12, 31)
print(start)
data = start
dat = start
while data < end:
    if data.weekday() == 4 and data.day == 1:
        dat = data
        break
    data = data + timedelta(1)
count = 0
dates = []
while dat < end:
    if dat.day == 1 and dat.month in [1,3,5,7,8,10,12]:
        dates.append(dat.strftime("%b"))
        count += 1
    dat = dat + timedelta(weeks=1)


print(dates)
print(dates[0], dates[-1], count)



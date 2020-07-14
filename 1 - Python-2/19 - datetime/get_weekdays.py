from datetime import date, timedelta

start = date(2020, 1, 1)
end = date(2021, 1, 1)

sundays = []

for day in range(366):
    #print(timedelta(day))
    next_day = start + timedelta(day)
#    if next_day.weekday() == 6: # sunday
    if next_day.weekday() in [5,6]: # saturday, sunday
        sundays.append(next_day)
        print(next_day)

from datetime import date, timedelta

def num_of_leapyears(s):
    years = s.split("-")
    count_leap_years = 0
    year = int(years[0])
    while year <= int(years[1]):
        last_day_february = date(year, 3, 1) - timedelta(days=1)
        if last_day_february.day == 29:
            count_leap_years += 1
        year += 1
    return count_leap_years


print(num_of_leapyears("1980-1984"))
print(num_of_leapyears("2000-2020"))
print(num_of_leapyears("1600-2000")) #98

# 2 case:
import calendar
leap = 0
for year in range(1600, 2001):
    if calendar.isleap(year):
        leap += 1
print(leap) # 98
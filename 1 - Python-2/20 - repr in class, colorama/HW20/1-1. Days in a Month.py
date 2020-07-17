from datetime import date, timedelta


def days(month, year):
    if month < 12:
        last_day_of_month = date(year, month+1, 1) - timedelta(days=1)
    else:
        last_day_of_month = date(year+1, 1, 1) - timedelta(days=1)

    return last_day_of_month.day


print(days(2, 2018))
print(days(4, 654))
print(days(2, 200))
print(days(2, 1000))
print(days(2, 2020))
print(days(3, 2020))
print(days(12, 2020))
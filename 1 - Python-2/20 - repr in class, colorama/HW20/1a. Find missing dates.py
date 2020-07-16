import datetime
from datetime import date, timedelta
from random import randint, sample


def find_missing_dates(dates_list):
    earliest = min(dates_list)
    latest = max(dates_list)

    missing_dates = []
    date = earliest
    while date <= latest:
        if date not in dates_list:
            missing_dates.append(date)
        date += timedelta(days=1)

    return missing_dates


def gen_dates_list():
    today = date.today() + timedelta(randint(-10, 10))
    dates = [today + timedelta(i) for i in range(randint(15, 25))]
    return sample(dates, randint(10, 15))


dates_list = gen_dates_list()
print("Dates list:")
print(sorted(dates_list))
print("Missing dates:")
print(sorted(find_missing_dates(dates_list)))
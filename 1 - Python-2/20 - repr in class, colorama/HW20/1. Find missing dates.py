from datetime import date, timedelta

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

dates_list = [date(2020, 7, 20),
              date(2020, 7, 18),
              date(2020, 7, 23),
              date(2020, 7, 21),
              date(2020, 7, 16)]


print(find_missing_dates(dates_list))

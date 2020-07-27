from datetime import datetime, date, timedelta

year = 2015
start = datetime(year, 1, 1)
end = datetime(year, 12, 31)

data = start
count_fridays = 0
while data <= end:
    print(data)
    week_day = datetime.weekday(data)
    day = data.strftime("%d")
    print(week_day)
    print(day)
    if day == "13" and week_day == 4:
        count_fridays += 1
    data += timedelta(1)

print(f"Number of fridays in {year}: {count_fridays}")


def unlucky_days(year):
    return sum(date(year, m, 13).weekday() == 4 for m in range(1, 13))


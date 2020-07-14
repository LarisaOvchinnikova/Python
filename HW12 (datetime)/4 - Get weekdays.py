from datetime import date, timedelta

start = date(2020, 1, 1)
end = date(2020, 12, 31)

i = start
while i <= end:
    first_day = i.strftime("%d")
    if first_day == "01":
        print(i.strftime("%B %d: %A"))
    i = i + timedelta(days=1)

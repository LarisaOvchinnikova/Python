from datetime import datetime, date

def get_day(element):
    return element.day

dates = [date(2018, 10, 5), date(2018, 7, 20),
        date(2000, 8, 25), date(2018, 4, 21),
        date(2003, 4, 11), date(2020, 3, 8),
        date(2008, 3, 18)]

print(sorted(dates,key=get_day))
# или:
print(sorted(dates, key=lambda el: el.day))

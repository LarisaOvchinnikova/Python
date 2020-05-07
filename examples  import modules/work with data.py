from datetime import datetime, date
#import datetime

print(datetime.today())
today = datetime.today()
print(str(today))
print(today.year)
print(today.day)
print(today.month)


today = date.today()
print(today)
print(today.month)
new_year = date(2021,1,1)
print(new_year)
print(new_year - today)
print((new_year - today).days)
today = datetime.today()

if today == new_year:
    print("Happy New Year")
else:
    print(f"It's still {(new_year - today).days} days until New Year")

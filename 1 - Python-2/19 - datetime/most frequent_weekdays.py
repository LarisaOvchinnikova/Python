from datetime import date, timedelta
year = 1984
start = date(1984, 1, 1)
end = date(2021, 1, 1)

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    n = 366
else:
    n = 365
days = []

for day in range(n):
    next_day = start + timedelta(day)
    name = next_day.strftime("%A")
    print(name)
    # days.append(next_day.weekday())
    days.append(name)
print(days)
obj ={el:days.count(el) for el in days}
# for el in days:
#     if el in obj:
#         obj[el]+=1
#     else:
#         obj[el]=1
print(obj)
print(sorted(obj.items(), key=lambda el:el[1]))
print(max(obj.values()))
res = [el[0] for el in obj.items() if el[1] == max(obj.values())]
print(res)
print(len(days))
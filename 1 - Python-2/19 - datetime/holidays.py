from datetime import datetime, timedelta

dates = """
    New Year's Day                Wed, Jan 1, 2020
    Martin Luther King Jr. Day    Mon, Jan 20, 2020
    Memorial Day                    Mon, May 25, 2020
    Independence Day                Fri, Jul 3, 2020
    Labor Day                      Mon, Sep 7, 2020
    Veterans Day                    Wed, Nov 11, 2020
    Thanksgiving                    Thu, Nov 26, 2020
    Christmas Day                  Fri, Dec 25, 2020
    """

dates = [name.strip() for name in dates.split("  ") if name.strip() != ""] # Сплитим строку dates и создаем список из названий праздников и их дат, убираем все пробелы и отступы.

data_dict = {dates[i]: dates[i+1] for i in range(0, len(dates), 2)}

holidays = {}
for key, value in data_dict.items():
    holidays[datetime.strptime(value, "%a, %b %d, %Y")] = key
## Cоздем словарь, где ключом будет date, а значением название праздника.


today = input("Enter the date.\nInput must look like this: '2020, Sep 23'\n")
today = datetime.strptime(today, "%Y, %b %d") # переводим инпут в тип datetime


if today in holidays: # если в словаре есть ключ с такой датой, тогда сразу поздравляем с праздником.
    print(f"Happy {holidays[today]}!")
else:
    wait_time = min([date - today for date in holidays.keys() if date > today]) # находим минимальную timedelta которая больше 0
    print(f"Good news! There are {wait_time.days} days until the {holidays[today+wait_time]}")  # получаем название по ключу из сегодняшней даты + timedelta дней до праздника


from datetime import datetime, date, timedelta
holidays = """
    New Year's Day                Wed, Jan 1, 2020
    Martin Luther King Jr. Day    Mon, Jan 20, 2020
    Memorial Day                  Mon, May 25, 2020
    Independence Day              Fri, Jul 3, 2020
    Labor Day                     Mon, Sep 7, 2020
    Veterans Day                  Wed, Nov 11, 2020
    Thanksgiving                  Thu, Nov 26, 2020
    Christmas Day                 Fri, Dec 25, 2020
    """

holidays = holidays.split("   ")
holidays = [el.strip() for el in holidays if el.strip() != ""]
holiday_dates = [el for i, el in enumerate(holidays) if i % 2 != 0]

holiday_dates = [datetime.strptime(el, "%a, %b %d, %Y") for el in holiday_dates]
holiday_dates = [el.strftime("%Y-%d-%m") for el in holiday_dates]

start = date(2020, 1, 1)
end = date(2020, 12, 31)

data = start
count_work_days = 0
while data <= end:
    day_of_week = data.strftime("%A")
    day = data.strftime("%Y-%d-%m")
    if day_of_week not in ["Saturday", "Sunday"] and day not in holiday_dates:
        count_work_days += 1

    data += timedelta(days=1)

print(f"Number of work days in 2020: {count_work_days}")

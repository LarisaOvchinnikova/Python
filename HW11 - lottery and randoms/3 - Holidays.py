# import datetime
from datetime import datetime, date, timedelta
holidays = {
"New Year's Day": "Wed, Jan 1, 2020",
"Martin Luther King Jr. Day": "Mon, Jan 20, 2020",
"Memorial Day": "Mon, May 25, 2020",
"Independence Day": "Fri, Jul 3, 2020",
"Labor Day": "Mon, Sep 7, 2020",
"Veterans Day": "Wed, Nov 11, 2020",
"Thanksgiving": "Thu, Nov 26, 2020",
"Christmas Day": "Fri, Dec 25, 2020"
}
#print(holidays)
# for key in holidays.keys():
#     print(key)
# for value in holidays.values():
#     print(value)
# for key, value in holidays.items():
#     print(key, value)


today = datetime.today()
print(today)
# today = date.today()
# print(today)
today = datetime.strftime(today, "%b %d %Y")
print(today)
new_year = datetime.strptime("Jan 1 2020", "%b %d %Y")
print(new_year)
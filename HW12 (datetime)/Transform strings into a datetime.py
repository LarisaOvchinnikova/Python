from datetime import datetime
# strptime(строка, формат) ---> перевод строки в datetime
day1 = "March 29 2020"
d1 = datetime.strptime(day1, "%B %d %Y")
print(d1)

day2 = "Oct 12, 1994"
d2 = datetime.strptime(day2, "%b %d, %Y")
print(d2)

day3 = "12 12 2012"
d3 = datetime.strptime(day3, "%m %d %Y")
print(d3)

day4 = "Wed, April 4, 84"
d4 = datetime.strptime(day4, "%a, %B %d, %y")
print(d4)

day5 = "01/01/2000"
d5 = datetime.strptime(day5, "%m/%d/%Y")
print(d5)

day6 = "Sep 1 1872 14:30"
d6 = datetime.strptime(day6, "%b %d %Y %H:%M")
print(d6)

day7 = "2009, 29 Nov, 11:20 PM"
d7 = datetime.strptime(day7, "%Y, %d %b, %I:%M %p")
print(day7)
print(type(d7))

day8 = "Saturday, February 9, 2020. 13:48:09"
d8 = datetime.strptime(day8, "%A, %B %d, %Y. %H:%M:%S")
print(d8)




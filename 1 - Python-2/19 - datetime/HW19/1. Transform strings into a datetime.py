from datetime import datetime

day1 = "March 29 2020"
print(datetime.strptime(day1, "%B %d %Y"))

day2 = "Oct 12, 1994"
print(datetime.strptime(day2, "%b %d, %Y"))

day3 = "12 12 2012"
print(datetime.strptime(day3, "%m %d %Y"))

day4 = "Wed, April 4, 84"
print(datetime.strptime(day4, "%a, %B %d, %y"))

day5 = "01/01/2000"
print(datetime.strptime(day5, "%m/%d/%Y"))

day6 = "Sep 1 1872 14:30"
print(datetime.strptime(day6, "%b %d %Y %H:%M"))

day7 = "2009, 29 Nov, 11:20 PM"
print(datetime.strptime(day7, "%Y, %d %b, %I:%M %p"))

day8 = "Saturday, February 9, 2020. 13:48:09"
print(datetime.strptime(day8, "%A, %B %d, %Y. %H:%M:%S"))


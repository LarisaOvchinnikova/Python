def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days(month, year):
    return 30 if month in [4, 6, 9, 11] else 31 if month in [1, 3, 5, 7, 8, 10, 12] else 29 if isLeapYear(year) else 28


print(days(2, 2018))
print(days(4, 654))
print(days(2, 200))
print(days(2, 1000))
print(days(2, 2020))
print(days(3, 2020))
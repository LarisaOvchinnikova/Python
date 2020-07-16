def isLeapYear(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_valid_date(year, month, day):
    y = year > 0
    m = 1 <= month <= 12
    d = 1 <= day <= 30 if month in [4, 6, 9, 11] else 1 <= day <= 31 if month in [1, 3, 5, 7, 8, 10, 12] else 1 <= day <= 29 if isLeapYear(year) else 1 <= day <= 28
    return y and m and d

print(is_valid_date(2020, 15, 2)) # False (month = 15)
print(is_valid_date(-2020, 5, 4)) # False (year < 0)
print(is_valid_date(2020, 4, 31)) # False (no 31 in April)
print(is_valid_date(2020, 4, 30)) # True
print(is_valid_date(2020, 2, 29)) # True  (2020/2/29 exist because 2020 is leap year)
print(is_valid_date(2019, 2, 29)) # False  (2019/2/29 doesn't exist because 2019 is not a leap year)
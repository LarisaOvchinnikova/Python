from datetime import  date

def is_valid_date(year, month, day):
    try:
        day_check = date(year, month, day)
    except ValueError:
        return False
    return True

print(is_valid_date(2020, 15, 2)) # False (month = 15)
print(is_valid_date(-2020, 5, 4)) # False (year < 0)
print(is_valid_date(2020, 4, 31)) # False (no 31 in April)
print(is_valid_date(2020, 4, 30)) # True
print(is_valid_date(2020, 2, 29)) # True  (2020/2/29 exist because 2020 is leap year)
print(is_valid_date(2019, 2, 29)) # False  (2019/2/29 doesn't exist because 2019 is not a leap year)
def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def num_of_leapyears(s):
    years = s.split("-")
    count_leap_years = 0
    year = int(years[0])
    while year <= int(years[1]):
       if isLeapYear(year):
           count_leap_years += 1
       year += 1
    return count_leap_years


print(num_of_leapyears("1980-1984"))
print(num_of_leapyears("2000-2020"))
print(num_of_leapyears("1600-2000"))
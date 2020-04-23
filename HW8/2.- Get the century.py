#Get the century
#Create a function that takes in a year and returns the correct century.
def getCentury(year):
    import math
    cent = math.ceil(year/100)
    if cent == 1 or cent == 21:
        letters = 'st'
    elif cent == 2 or cent == 22:
        letters = 'nd'
    else:
        letters = 'th'
    return f"{math.ceil(year/100)}{letters} century"
print(getCentury(1756))
print(getCentury(1555))
print(getCentury(1000))
print(getCentury(1001))
print(getCentury(2005))
print(getCentury(2103))
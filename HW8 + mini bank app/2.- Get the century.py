#Get the century
#Create a function that takes in a year and returns the correct century.
def getCentury(year):
    import math
    cent = math.ceil(year/100)
    cent = str(cent)
    print(cent[-1])
    if cent[-1] == "1" and cent != '11':
        letters = 'st'
    elif cent[-1] == "2" and cent != '12':
        letters = 'nd'
    elif cent[-1] == "3" and cent != '13':
        letters = "rd"
    else:
        letters = 'th'
    return f"{cent}{letters} century"
print(getCentury(1756))
print(getCentury(1555))
print(getCentury(1000))
print(getCentury(1001))
print(getCentury(2005))
print(getCentury(2103))
print(getCentury(2299))
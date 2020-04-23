#Get the century
#Create a function that takes in a year and returns the correct century.
def getCentury(year):
    import math
    return math.ceil(year/100)
print(getCentury(1756))
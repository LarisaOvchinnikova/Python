tank = float(input("How many gallons? "))
mpg = float(input("What is miles per gallon? "))
miles = tank * mpg
print("You can drive", miles, "miles")
price = float(input("Print price per gallon"))
money = price * tank
print("Your tank cost is", money)
distance = float(input("What is distance to gas station?"))
if miles < distance:
    print("you can not get gas station ")
else: print("you have enough gas")

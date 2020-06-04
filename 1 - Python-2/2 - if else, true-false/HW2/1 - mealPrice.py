mealPrice = float(input("Enter meal price "))
tipPercent = int(input("Enter tip percent "))
taxPercent = int(input("Enter tax percent "))
mealCost = mealPrice*( 1 + tipPercent / 100 + taxPercent / 100);
print(f"The total cost: ${round(mealCost, 2)}")

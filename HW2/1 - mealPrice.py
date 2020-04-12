mealPrice = float(input("input meal price "))
tipPercent = int(input("input tip percent "))
taxPercent = int(input("input tax percent "))
mealCost = mealPrice + mealPrice * tipPercent / 100 + mealPrice * taxPercent / 100;
print(f"Total cost: ${round(mealCost, 2)}")

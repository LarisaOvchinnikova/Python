price = float(input("Enter price: "))
if price >= 300:
    discount = 30
elif price >= 200:
    discount = 20
elif price >= 50:
    discount = 10
elif price >= 0:
    discount = 0
    print("No discount")
else: print("Error")
total = price - price * discount / 100
print(f"total price = {total}")


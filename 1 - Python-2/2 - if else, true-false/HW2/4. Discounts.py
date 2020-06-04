price = int(input("Enter price: "))
if price >= 300:
  total = price * 0.7
elif price >= 200:
  total = price * 0.8
elif price >= 100:
  total = price * 0.9
elif price >= 0:
  total = price
else:
  total = "Error"
print(total)
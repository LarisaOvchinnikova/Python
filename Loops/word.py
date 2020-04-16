name = "121"
digit = 0
upper = 0
lower = 0
for char in name:
    if char.isdigit():
        digit += 1
    if char.isupper():
        upper += 1
    if char.islower():
        lower += 1
print(digit)
print(upper)
print(lower)

if digit and not upper and not lower:
    print("Has only digits")
if digit == len(name) and len(name) > 0:
    print("Has only digits")

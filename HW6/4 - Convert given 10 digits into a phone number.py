def phone_number(num):
    return f"({num[0:3]}) {num[3:6]}-{num[6:]}"

number = "5053452936"
print(phone_number(number))   # "(505) 345-2936"
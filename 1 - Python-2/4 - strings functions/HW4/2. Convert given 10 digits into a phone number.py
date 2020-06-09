# #2. Convert given 10 digits into a phone number
# number = "5053452936"
# Turn it into "(505) 245-2936"

def phone_number(number):
    number = str(number)
    return f"({number[:3]}) {number[3:6]}-{number[6:]}"
print(phone_number(1234567890))
print(phone_number("9542223433"))
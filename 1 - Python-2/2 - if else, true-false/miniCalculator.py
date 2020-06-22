num1 = int(input("Input first number"))
num2 = int(input("Input second number"))
operation = input("Input arithmetical operation")
if operation == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == '*':
     print(f"{num1} * {num2} = {num1 + num2}")
elif operation == '/':
    print(f"{num1} / {num2} = {num1 / num2}")
elif operation == '%':
    print(f"{num1} % {num2} = {num1 % num2}")
else: print("Invalid operation")

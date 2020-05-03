a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter arithmetical operation: ")

res = {
    '+': a + b,
    '-': a - b,
    '*': a * b,
    '/': a / b
}.get(op)

print(res)

def celsius_to_fahrenheit(x):
    return x*1.8 + 32.2
x = input("Enter temperature: ")

while not x.isdigit():
    print("Wrong value. Try again")
    x = input("Enter temperature: ")

x = int(x)
print(f"{x}C = {celsius_to_fahrenheit(x)}F")

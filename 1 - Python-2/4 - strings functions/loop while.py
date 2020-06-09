while True:
    name = input("Enter your name: ")
    if name.isalpha():
        break
print(f"Hello {name}")

while True:
    degrees = input("Enter degrees: ")
    if degrees.lower() == "exit":
        break
    if not degrees.isdigit():
        continue
    degrees = int(degrees)
    print(degrees)
print("Goodbye")
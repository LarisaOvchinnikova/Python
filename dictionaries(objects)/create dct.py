dct = {}
n = int(input("Enter number of people: "))
for i in range(1, n+1):
    name = input(f"Enter name of {i} person: ")
    vacation = input(f"Where does {name} want to go on vacation? ")
    dct[name] = vacation

print(dct)

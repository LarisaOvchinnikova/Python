# Print firstname, middlename, lastname in column
firstName = input("What is your first name? ")
middleName = input("What is your middle name? ")
lastName = input("What is your last name? ")

m = max(len(firstName), len(lastName), len(middleName))
print(firstName.rjust(m))
print(middleName.rjust(m))
print(lastName.rjust(m))

print(f"{firstName.rjust(m)}\n{middleName.rjust(m)}\n{lastName.rjust(m)}")
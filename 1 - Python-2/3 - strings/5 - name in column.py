def in_column(firstName, middleName, lastName):
    m = max(len(firstName), len(lastName), len(middleName))
    return f"{firstName.rjust(m)}\n{middleName.rjust(m)}\n{lastName.rjust(m)}"


firstName = input("What is your first name? ")
middleName = input("What is your middle name? ")
lastName = input("What is your last name? ")
print(in_column(firstName, middleName, lastName))

year = input("Enter the year: ")
name = input("Enter the name: ")
x = open(f"babynamesranking{year}.txt")


text = x.readlines()
fl = False
for string in text:
    if name not in string:
        continue
    else:
        fl = True
        names = string.split()
        i = names.index(name)
        print(f"{name} is ranked #{names[0]} in year {year}")
        if i == 1:
            gender = "boys"
        else:
            gender = "girls"
        print(f"{names[i+1]} {gender} named {name}!")
        break

if not fl:
    print(f"The name {name} is not ranked in year {year}")
year = input("Enter the year: ")
name = input("Enter the name: ")
x = open(f"babynamesranking{year}.txt")
t = x.readlines()

if not name in t:
    print(f"The name {name} is not ranked in year {year}")
else:

    names = [el.split() for el in text if name in el]
    print(text)
    print(names)
    print(names[0])
    i = names[0].index(name)
    print(i)
    print(f"{name} is ranked #{names[0][0]} in year {year}")
    if i == 1:
        gender = "boys"
    else:
        gender = "girls"
    print(f"{names[0][i+1]} {gender} named {name}!")
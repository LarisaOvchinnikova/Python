person = {
    "name": "Alice",
    "age": 25,
    "isAdult": True,
}
for key in person:
    print(key)
# dictionary comprehension - упрощение
# {key: value for key, value in dict.items()}

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
                  "December"]
dct = {i + 1: month for i, month in enumerate(month_list) }
print(dct)
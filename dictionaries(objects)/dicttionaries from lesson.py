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
dct1 = {i + 1: month for i, month in enumerate(month_list) }
print(dct1)

dct = {month: i+1 for i, month in enumerate(month_list)}
print(dct)

# увеличим значения на 10
for month in dct.keys():
    dct[month] *= 10
print(dct)

# сделаем с помощью list comprehension
dct = {month: value * 10 for month, value in dct.items() }
print(dct)

# посчитать количество слов в строке с помощью list comprehension
text = "sky is blue"
print(text.count("s"))

dct = {key: text.count(key) for key in text}
print(dct)
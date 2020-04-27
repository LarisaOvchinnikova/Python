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

# посчитать количество букв в строке с помощью list comprehension
text = "sky is blue"
print(text.count("s"))

dct = {letter: text.count(letter) for letter in text}
print(dct)

# count words in text:
text = "sun is yellow and sun is hot"
arr = text.split(' ')
print(arr)
dct ={word: arr.count(word) for word in arr}
print(dct)
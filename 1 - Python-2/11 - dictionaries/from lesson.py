names = {
    "Jack": 29,
    "Mark": 32,
    "Sara": 29,
}

print(names) # {'Jack': 29, 'Mark': 32, 'Sara': 29}
print(names["Sara"])  # 29

print("Anna" in names) # False

if "Anna" in names:
    print(names["Anna"])
else:
    names["Anna"] = 23    # добавили пару key:value ("Anna": 23)

print(names)


#Removing elements
del names["Sara"]
print(names)


# посчитаем элементы: сколько раз встречается каждая буква в строке

text = "The sky is blue"

counts = {}
for letter in text:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1
print(counts)
# result:
#{'T': 1, 'h': 1, 'e': 2, ' ': 3, 's': 2, 'k': 1, 'y': 1, 'i': 1, 'b': 1, 'l': 1, 'u': 1}

text = "The roses are red and roses are nice"
dct = {}
for word in text.split():
    if word in dct:
        dct[word] += 1
    else:
        dct[word] = 1

arr_keys = []
arr_values = []
for key in dct:
    print(key)
    arr_keys.append(key)
    print(dct[key])
    arr_values.append(dct[key])

print(arr_keys)
print(arr_values)

# превращение словаря в список из ключей,значений, пар
print(dct.keys())  # dict_keys(['The', 'roses', 'are', 'red', 'and', 'nice'])
print(list(dct.keys()))  # ['The', 'roses', 'are', 'red', 'and', 'nice']

print(dct.values()) # dict_values([1, 2, 2, 1, 1, 1])
print(list(dct.values()))  # [1, 2, 2, 1, 1, 1]

print(dct.items()) # dict_items([('The', 1), ('roses', 2), ('are', 2), ('red', 1), ('and', 1), ('nice', 1)])
print(list(dct.items())) # [('The', 1), ('roses', 2), ('are', 2), ('red', 1), ('and', 1), ('nice', 1)]

for person, age in names.items():  # итерация по ключам и значениям
    print("Hello", person)
    print(f"You are {names[person]} years old")



names = {}
names["Ann"] = 33
print(names)
names["Yury"] = names.get("Yury", 35) + 1
print(names)


# ----
x = dict()
print(x)  # {}

# ----
y = dict([('m', 8), ('n', 9)])
print(y)
x = dict(name = "John", age = 36, country = "Norway")
print(x)

dct = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}
arr = list(dct.values())  # [71, 45, 15, 29]
print(arr)

print(dct.values())
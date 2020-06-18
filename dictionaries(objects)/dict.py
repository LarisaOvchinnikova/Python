dict = {
    'name': "Bob",
    "age": 12,
}
for word in dict:
    print(word)
# name
# age

print('---1--')
for value in dict.values():
    print(value)
# Bob
# 12
print(dict.keys())
#dict_keys(['name', 'age'])

print(dict.values())
#dict_values(['Bob', 12])

print(dict.items())
#dict_items([('name', 'Bob'), ('age', 12)])
#- ---
print(dict)
# {'name': 'Bob', 'age': 12}

for key in dict.keys():
    dict[key] *= 10
print(dict)
# {'name': 'BobBobBobBobBobBobBobBobBobBob', 'age': 120}

dct = {}
text = 'roses are nice and flowers are red'
for index, letter in enumerate(text):
    # print(letter, index)
    dct[letter] = index
print(dct)
#{'r': 31, 'o': 21, 's': 25, 'e': 32, ' ': 30, 'a': 27, 'r': 31, 'n': 16, 'i': 11, 'c': 12, 'd': 33, 'f': 19, 'l': 20, 'w': 22}

#---------
for key, value in dict.items():
    print(key, value)
# name BobBobBobBobBobBobBobBobBobBob
# age 120


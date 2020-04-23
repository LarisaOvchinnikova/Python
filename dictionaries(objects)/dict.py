dict = {
    'name': "Bob",
    "age": 12,
}
for word in dict:
    print(word)
for value in dict.values():
    print(value)
print(dict.keys())
print(dict.values())
print(dict.items())
#- ---
print(dict)
for key in dict.keys():
    dict[key] *= 10
print(dict)
#---=-
dct = {}
text = 'Roses are nice and flowers are red'
for index, letter in enumerate(text):
    print(letter, index)
    dct[letter] = index
print(dct)
#---------
for key, value in dict.items():
    print(key, value)
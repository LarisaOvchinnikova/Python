def filter_vowel(lst):
    arr = [el for el in lst if el[0].lower() in "aeuio"]
    return arr

items = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
filtered_list = filter_vowel(items)
print(filtered_list)
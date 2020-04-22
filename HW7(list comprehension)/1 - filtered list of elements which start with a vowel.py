# Use list comprehension to create a filtered list of
# elements which start with a vowel.
list = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
vowels = 'aeuio'
filtered_list = [word for word in list if word[0].lower() in vowels]
print((filtered_list))
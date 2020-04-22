# Use list comprehension to create a list of tuples
# of first and last letter of the word

input = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
output = [(word[0], word[-1]) for word in input]
print(output)
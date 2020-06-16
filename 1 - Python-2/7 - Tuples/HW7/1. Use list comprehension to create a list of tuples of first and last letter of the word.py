def list_tuples(arr):
    return [(el[0], el[-1]) for el in arr]


print(list_tuples(['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']))
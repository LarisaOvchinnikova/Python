def filter_len(lst):
    arr = [el for el in lst if len(el) < 5]
    return arr

items = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
filtered_list = filter_len(items)
print(filtered_list)
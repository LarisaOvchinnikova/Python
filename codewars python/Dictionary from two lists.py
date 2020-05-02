def createDict(keys, values):
    dct = {}
    while len(keys) > len(values):
        values.append(None)
    for i, key in enumerate(keys):
        dct[key] = values[i]
    return dct

print(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]))
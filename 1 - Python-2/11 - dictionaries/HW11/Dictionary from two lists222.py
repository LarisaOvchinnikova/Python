def createDict(keys, values):
    values = values + [None] * (len(keys) - len(values))
    return {keys[i]: values[i] for i in range((len(keys)))}



keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
print(createDict(keys, values)) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
print(createDict(keys, values)) # returns {'a': 1, 'b': 2, 'c': 3}
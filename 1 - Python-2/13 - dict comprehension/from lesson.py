print({i: i+2 for i in range(5)})  #  {0: 2, 1: 3, 2: 4, 3: 5, 4: 6}

arr = ['a', 'b', 'c']
dct = {el: i for i, el in enumerate(arr)}
print(dct)  #    {'a': 0, 'b': 1, 'c': 2}

square = {i: i**2 for i in range(1, 10)}
print(square)
#  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

square = {i: i**2 for i in range(10) if i % 2 != 0}
print(square)   #  {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

dct = {i: char for i, char in enumerate("sky is blue") if char != ' '}
print(dct) #   {0: 's', 1: 'k', 2: 'u', 4: 'i', 5: 's', 7: 'b', 8: 'l', 9: 'u', 10: 'e'}

dct = {char: i for i, char in enumerate("sky is blue") if char != ' '}
print(dct)  #  {'s': 5, 'k': 1, 'y': 2, 'i': 4, 'b': 7, 'l': 8, 'u': 9, 'e': 10}

dct_reversed = {value: key for key, value in dct.items()}
print(dct_reversed) # {5: 's', 1: 'k', 2: 'y', 4: 'i', 7: 'b', 8: 'l', 9: 'u', 10: 'e'}



# Find programmers with common languages
def commmon_languages(dct):
    arr = []
    for values in dct.values():
        print(values)
        x = set(values)
        print(x)
        arr.append(x)
    res = arr[0]
    for el in arr:
        res = res & el
    return res

print(commmon_languages({
    'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
'paul': ['C++', 'JS', 'Python'],
'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
'tim': ['Python', 'Haskell', 'C++', 'JS']
}))
# Find programmers with common languages
def commmon_languages(dct):
    common = set(list(dct.values())[0])
   # common = {}
    for values in dct.values():
       # if len(common) == 0:
       #     common = set(values)
        common = common & set(values)
    return common
print(commmon_languages({

'bob': ['JS', 'PHP', 'Python', 'Perl', 'Java'],
'paul': ['C++', 'JS', 'Python'],
'sara': ['Perl', 'C', 'Java', 'Python', 'JS'],
'tim': ['Python', 'Haskell', 'C++', "JS"]
}))
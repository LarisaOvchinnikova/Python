def anagrams(word, words):
    match = {}
    for char in word:
        match[char] = word.count(char)
    res = []
    for w in words:
        dct = {}
        for letter in w:
            dct[letter] = w.count(letter)
        if match == dct:
            res.append(w)
    return res


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
def anagrams(word, words):
    match = {}
    for char in word:
        match[char] = word.count(char)
    dct = {'a': 2, 'b': 2}
    dct1  = {'b': 2, 'a': 2}
    return dct1 == dct

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
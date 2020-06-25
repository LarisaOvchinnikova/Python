def count_words(text):
    dct = {}
    for word in text.lower().split():
        if word in dct:
            dct[word] += 1
        else:
            dct[word] = 1
    return dct


text = "Roses are red violets are blue"
print(count_words(text))
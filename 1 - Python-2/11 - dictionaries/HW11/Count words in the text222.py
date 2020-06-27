# def count_words(text):
#     dct = {}
#     for word in text.lower().split():
#         if word in dct:
#             dct[word] += 1
#         else:
#             dct[word] = 1
#     return dct

def count_words(text):
    dct = {}
    for word in text.lower().split():
        dct[word] = dct.get(word, 0) + 1

    return dct


text = "Roses are red violets are blue"
print(count_words(text))


names = {
    "Mark": 12,
    "Sarah": 13,
}
print(names["Mark"])
print(names.get("Mark"))
print(names.get("Mark", 0)) # 12
print(names.get("Jack"))   # None
print(names.get("Jack", 0)) # 0
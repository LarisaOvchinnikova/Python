import operator
def find_occurrences(text, letter):
    text = text.lower()
    letter = letter.lower()
    arr = text.split()
    dct = {word:word.count(letter) for word in arr}
    return dct

# print(find_occurrences("Hello World", "o"))
# print(find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A") )
def letter_frequency(text):
    text = text.lower().replace(" ", "")
    dct = {letter:text.count(letter) for letter in text}
    # arr = sorted(list(dct.items()), key=lambda el: el[1], reverse=True)
    arr = sorted(list(dct.items()), key=operator.itemgetter(1))[::-1]
    print(arr)

print(letter_frequency('wklv lv d vhfuhw phvvdjh'))
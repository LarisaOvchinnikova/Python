def find_occurrences(text, letter):
    text = text.lower()
    letter = letter.lower()
    arr = text.split()
    dct = {word:word.count(letter) for word in arr}
    return dct

print(find_occurrences("Hello World", "o"))
print(find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A") )
def find_occurrences(text, letter):
    text = text.lower()
    letter = letter.lower()
    words = text.split()
    dct = {word: word.count(letter) for word in words}
    return dct

print(find_occurrences("Hello World", "o"))
print(find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A") )
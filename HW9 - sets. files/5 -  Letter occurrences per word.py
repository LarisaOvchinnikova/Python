def find_occurrences(text, letter):

    arr = text.split()
    dct = {word:word.count(letter) for word in arr}
    return dct

print(find_occurrences("Hello World", "o"))
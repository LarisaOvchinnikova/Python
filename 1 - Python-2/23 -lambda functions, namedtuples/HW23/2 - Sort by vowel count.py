def vowel_count(word):
    vowels = "aeuio"
    word = word.lower()
    return sum([1 if letter in vowels else 0 for letter in word])

text = "a b abc aeu bd aaaa abcd"
print(sorted(text.split(), key=vowel_count))

text = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation aaaaa ullamco laboris 
nisi ut aliquip ex ea commodo consequat."""
print(sorted(text.split(), key=vowel_count))
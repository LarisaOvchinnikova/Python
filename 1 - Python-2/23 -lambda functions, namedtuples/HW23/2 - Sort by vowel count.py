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
print(sorted(text.split(),
             key=lambda word: len([char for char in word if char.lower() in "aeuio"])))

print(sorted(text.split(),
             key=lambda word: sum([char.lower() in "aeuio" for char in word])))

# сортировка по количеству гласных букв и  по алфавиту
# два параметра сортировки как тапл в круглых скобках через запятую)

print(sorted(text.split(),
             key=lambda word: (sum([char.lower() in "aeuio" for char in word]), word)))
# сортировка по количеству гласных букв, а потом по длине слова)

print(sorted(text.split(),
             key=lambda word: (sum([char.lower() in "aeuio" for char in word]), len(word))))
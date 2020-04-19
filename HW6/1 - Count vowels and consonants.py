def count_vowels_and_consonants(name):
    vowels = 'aeuio'
    countVowels = 0
    for i in name:
      if i in vowels:
         countVowels += 1
    return f"Hello {name}! There are {countVowels} vowels and {len(name) - countVowels} consonants in your name"


name = input("What is your name? ")
print(count_vowels_and_consonants(name))
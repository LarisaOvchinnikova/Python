def count_vowels_and_consonants(name):
    vowels = 0
    for el in name:
        if el in "aeuio":
            vowels += 1
    return f"Hello {name}, there are {vowels} vowels and {len(name) - vowels} consonants in your name."

print(count_vowels_and_consonants("Larisa"))
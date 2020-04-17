def get_words_starting_with_vowel(lst):
    filtered_list = []
    vowels = "aeuio"
    for i in lst:
        if i[0].lower() in vowels:
            filtered_list.append(i)
    return filtered_list


print(get_words_starting_with_vowel(['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']))


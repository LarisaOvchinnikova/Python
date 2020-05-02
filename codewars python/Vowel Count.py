def getCount(inputStr):
    num_vowels = 0
    vowels = "aeiou"
    for letter in inputStr:
        if letter in vowels:
            num_vowels += 1

    return num_vowels
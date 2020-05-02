def disemvowel(string):
    vowels = "aeuio"
    return "".join([letter for letter in string if not letter.lower() in vowels])
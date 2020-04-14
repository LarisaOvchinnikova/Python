word = input("Enter word: ")
if word.islower() and word.isalpha():   # all characters are lowercase letters
    print(f"word \"{word}\" has only lowercase letters")
elif word.isupper() and word.isalpha(): # all characters are uppercase letters
    print(f"word \"{word}\" has only uppercase letters")
elif word.isalpha():    # all characters are alphabetic
    print(f"word \"{word}\" has so many letters(has both uppercase and lowercase letters but no digits). Much wow.") #!!
elif word.isdigit():    # all characters are digits
    print(f"word \"{word}\" has only digits")
elif word.islower():    # digits and lowercase letters
    print(f"word \"{word}\" has digits and only lowercase letters")
elif word.isupper():    # digits and uppecase letters
    print(f"word \"{word}\" has digits and only uppercase letters")
elif word.isalnum():    # letters and digits
    print(f"word \"{word}\" has all kinds of stuff")


if word.isdigit():
    print(f"word \"{word}\" has only digits")
elif word.isalpha():
    if word.islower():
        print("Only lowercase")
    elif word.isupper():
        print("hase onle uppercase")
    else:
        print("yas lowercase and uppercase")
elif word.isalnum():
    if word.islower():
        print("Has only lowercase and digits")
    elif word.isupper():
        print ("has only uppercase and digits" )
    else: print("has upper and lower and digits")



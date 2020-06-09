#Print word " has lowercase letters" if it has only lowercase alphabet characters
# Print word " has uppercase letters"
# if it has only uppercase alphabet characters
# Print word " has so many letters. Much wow."
# if it has both uppercase and lowercase alphabet characters but no digits
# Print word " has digits" if
# it has only digits
# Print word " has digits and lowercase letters"
# if it has digits and only lowercase letters
# Print word " has digits and uppercase letters"
# if it has digits and only uppercase letters
# Print word " has all kinds of stuff"
# if it has digits and both uppercase and lowercase letters

word = input("Enter word: ")
if word.isdigit():
    print("Has digits")
elif word.isalpha():
    if word.islower():
        print("Has lowercase")
    elif word.isupper():
        print("Has uppercase")
    else:
        print("Has upper and lower")
elif word.isalnum():
    if word.islower():
        print("Has lowercase and digits")
    elif word.isupper():
        print("Has uppercase and digits")
    else:
        print("Has upper and lower and digits")

help()  #вызов помощи
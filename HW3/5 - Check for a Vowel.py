name = input("What is your name? ")
name = name.capitalize()
vowels = "AEUOI"
if " " in name:
    print("Enter only one name")
elif name[0] in vowels:
    print("Your name starts with vowel")
else:
    print("Your name starts with consonant")
# 2 case:
vowel = 'aeuio'
if name[0].lower() in vowel:
    print("Your name starts with vowel")
else:
    print("Your name starts with consonant")


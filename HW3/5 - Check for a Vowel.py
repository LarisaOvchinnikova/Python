name = input("What is your name? ")
name = name.capitalize()
vowels = "AEUOI"
if " " in name:
    print("Enter only one name")
elif name[0] in vowels:
    print("Your name starts with vowel")
else:
    print("Your name starts with consonant")


name = input("What is your name? ")
print(f"Hello {name}! Your name has {len(name)} letters.")

# Print reversed name
print(f"Your reverse name is {name[::-1]}")


# Print n-th character of a word
word = input("Enter word: ")
n = int(input("Enter number: "))
print(f"{n}-th character of a word {word} is {word[n]}")

# Print firstname, middlename, lastname in column
firstName = input("What is your first name? ")
middleName = input("What is your middle name? ")
lastName = input("What is your last name? ")

m = max(len(firstName), len(lastName), len(middleName))
print(firstName.rjust(m))
print(middleName.rjust(m))
print(lastName.rjust(m))

# Strip the string of first 3 and last 3 characters
word2 = input("Enter word: ")
print(word2[3:-3])

# Find space in phrase. Print first word in phrase
phrase = input("Enter phrase: ")
spaceIndex = phrase.index(' ')
print(f"First word is {phrase[0:spaceIndex]}")



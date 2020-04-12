# Find space in phrase. Print first word in phrase
phrase = input("Enter phrase: ")
spaceIndex = phrase.index(' ')
print(f"First word is {phrase[0:spaceIndex]}")
vowels ="aeuio"
name = "John"
vowelCount = 0
consonantCount = 0
for letter in name:
    if letter.lower() in vowels:
        vowelCount +=1
    else:
        consonantCount += 1
print(vowelCount)
print(consonantCount)


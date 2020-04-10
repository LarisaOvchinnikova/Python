name = input("What is your name? ")
print(f"Hello {name}! Your name has {len(name)} letters.")
print(f"Your reverse name is {name[::-1]}")


# Print n-th character of a word
word = input("Enter word: ")
n = int(input("Enter number: "))
print(f"{n}-th character of a word {word} is {word[n]}")

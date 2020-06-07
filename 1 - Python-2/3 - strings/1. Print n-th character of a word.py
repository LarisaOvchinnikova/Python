# Print n-th character of a word
word = input("Enter word: ")
n = int(input("Enter number: "))
if n < len(word):
    print(f"{n}-th character of a word {word} is {word[n]}")
else:
    print("Too much!")
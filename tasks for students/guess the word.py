from random import randint
arr = ["sun", "light"]
n = randint(0,1)
word = arr[n]
spaces = ["." for i in range(len(word))]
print("".join(spaces))
print("Guess the word: ")

while "." in spaces:
    letter = input("Enter letter: ")
    if letter in word:
        print("Yes, the word contains this letter")
        index = word.index(letter)
        for i in range(len(spaces)):
            if spaces[i] == '.':
                if i == index:
                    spaces[i] = word[index]
    else:
        print(f"No, there are no letter {letter} in this word")
    print("".join(spaces))

print("You won!")
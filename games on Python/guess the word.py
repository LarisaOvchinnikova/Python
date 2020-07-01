from random import randint
arr = ["computer", "tomato", "sunny", "light", "zebra", "crocodile", "panda", "monkey"]
n = randint(0, len(arr))
word = arr[n]
spaces = ["." for i in range(len(word))]
print("".join(spaces))
print("Guess the word: ")
attempts = 0
while "." in spaces:
    letter = input("Enter letter: ")
    attempts += 1
    if letter in word:
        print("Yes, the word contains this letter")
        countOfLetters = word.count(letter)
        indexes = [i for i in range(len(word)) if word[i] == letter]
        #print(indexes)
        index = word.index(letter)
        for i in range(len(spaces)):
            if spaces[i] == '.':
                # if i == index:
                #     spaces[i] = word[index]
                for i in indexes:
                    spaces[i] = word[i]
    else:
        print(f"No, there are no letter {letter} in this word")
    print("".join(spaces))

print("You won!")
print(f"You used {attempts} attempts")
from random import choice
arr = ["computer", "tomato", "sunny", "light", "zebra", "crocodile", "panda", "monkey"]
arr = ["cat", "crocodile", "bear", "monkey", "mouse", "lion","turtle","rat","racoon","penguin","kangaroo","panda","donkey", "hamster","zebra","elephant","goat","horse","sheep","deer","giraffe","koala","leopard","cheetah","ostrich","eagle","spider","tortoise","shark","whale","chicken", "rhinosorus", "marmot","pig","dolphin", "owl", "armadilo", "dog", "wolf", "cow", "skunk", "opossum", "camel", "alligator", "squirrel", "flamingo", "octopus", "squid", "snail", "hippopotamus", "yak"]

word = choice(arr)
# print(word)
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
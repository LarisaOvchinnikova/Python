import random

num = random.randint(0,10) # random integer [0-10]
print("I know the number from 0 to 10. What number I have?")
answer = -1
while not answer == num:
    answer = int(input("Guess the number: "))
    if answer < num:
        print("greater")
    elif answer > num:
        print("less")
    else:
        print(f"You got it! It is {num}")
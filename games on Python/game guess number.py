from random import randint

from datetime import datetime

print("Guess the secret number")
count = 0
x = randint(1, 100)

start = datetime.today()
while True:
    answer = int(input("Try to guess number: "))
    count += 1
    if answer > x:
        print("Too big")
    elif answer < x:
        print("Too small")
    if answer == x:
        print("You get it!")
        end = datetime.today()
        print(f"You needed {count} tries. It took {(end - start).seconds} seconds")
        break



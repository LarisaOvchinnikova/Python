import random
from datetime import datetime

print("Guess the secret number")
count = 1
x = random.randint(1, 100)
answer = int(input("Try to guess number: "))
start = datetime.today()
while answer != x:
    count += 1
    if answer > x:
        print("Too big")
    elif answer < x:
        print("Too small")
    answer = int(input("Try to guess number: "))
end = datetime.today()
print("You get it!")
print(f"You needed {count} attempts. It took {(end - start).seconds} seconds")
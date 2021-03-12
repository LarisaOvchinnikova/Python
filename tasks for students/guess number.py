# import random
from random import randint
from datetime import datetime, date, timedelta

#num = random.randint(0,100) # random integer [0-10]
num = randint(1, 100)
print("I know the number from 0 to 100. What number I have?")
answer = int(input("Guess the number: "))
start = datetime.today()
count = 1
while not answer == num:
    if answer < num:
        print("Too small")
    elif answer > num:
        print("Too big")
    answer = int(input("Guess the number: "))
    count += 1
end = datetime.today()
print(f"You got it! It is {num}")
diff = (end - start).seconds
print(f"It took you {diff} seconds. You had {count} tries")
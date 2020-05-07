import random
from datetime import datetime

print("Guess the number")
count = 1
x = random.randint(1, 100)
answer = int(input("Enter number: "))
start = datetime.today()
while answer != x:
    count += 1
    if answer > x:
        print("Too big")
    elif answer < x:
        print("Too small")
    answer = int(input("Enter number: "))
end = datetime.today()
print("You get it!")
print(f"You needed {count} attempts. You took {(end - start).seconds} seconds")
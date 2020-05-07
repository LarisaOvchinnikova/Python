import random
print("Guess the number")
count = 1
x = random.randint(1, 100)
answer = int(input("Enter number: "))
while answer != x:
    count += 1
    if answer > x:
        print("Too big")
    elif answer < x:
        print("Too small")
    answer = int(input("Enter number: "))
print("You get it!")
print(f"Count = {count}")
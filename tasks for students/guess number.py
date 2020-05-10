import random
from datetime import datetime, date, timedelta

num = random.randint(0,100) # random integer [0-10]
print("I know the number from 0 to 100. What number I have?")
answer = int(input("Guess the number: "))
start = datetime.today() # в начале программы
while not answer == num:
    if answer < num:
        print("greater")
    elif answer > num:
        print("less")
    answer = int(input("Guess the number: "))
end = datetime.today() #  в конце программы
print(f"You got it! It is {num}")
diff = (end - start).seconds
print(f"It took {diff} seconds")
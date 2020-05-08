import random
source_copy = []
lst = []
while len(lst) < 5:
    x = random.randint(1, 20)
    if not x in lst:
        lst.append(x)
        source_copy.append(x)
#print(lst)
print("I have a list of 5 numbers from 1 to 20, try to guess it")
print("You have 10 attempts")
right_answers = []
count = 0
for i in range(10):
    answer = int(input("Enter number from 1 to 20: "))
    if answer in lst:
        right_answers.append(answer)
        lst.remove(answer)
        count += 1
print(f"You guessed {count} numbers: {right_answers}")
print(f"List of numbers was: {source_copy}")
print(f"You have {5*count} points")
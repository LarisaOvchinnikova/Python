import random
sequence = []
length = random.randint(1, 15)
coefficient = random.randint(1, 20)
for i in range(length):
    sequence.append(i*coefficient)
# print(sequence)
x = random.randint(0, length - 1)
missed_number = sequence[x]
sequence[x] = "..."
print("Guess missed number: ")
print(sequence)
answer = int(input("Enter your answer: "))
if answer == missed_number:
    print("Good job!")
else:
    print("Try next time")

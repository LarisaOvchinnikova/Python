import random
attempts = int(input("How many times you want to play? "))
for i in range(attempts):
    sequence = []
    length = random.randint(3, 15)
    coefficient = random.randint(1, 20)
    for i in range(length):
        sequence.append(i*coefficient)

    x = random.randint(0, length - 1)
    missed_number = sequence[x]
    sequence[x] = "..."
    print("Guess missed number: ")
    print(sequence)
    answer = int(input("Enter your answer: "))
    while answer != missed_number:
        if answer > missed_number:
            print("Too big!")
        elif answer < missed_number:
            print("Too small")
        answer = int(input("Enter your answer: "))
    print("You got it!")
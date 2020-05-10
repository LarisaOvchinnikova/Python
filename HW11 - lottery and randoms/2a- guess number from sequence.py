import random
attempts = int(input("How many times you want to play? "))
for i in range(attempts):
    option = random.choice(["arithmetic", "geometric"])
    sequence = []
    n1 = random.randint(1,10)
    length = random.randint(5, 10)
    if option == "arithmetic":
        coefficient = random.randint(1, 15)
        for i in range(length):
            sequence.append(n1)
            n1 += coefficient
    else:
        coefficient = random.randint(2, 10)
        for i in range(length):
            sequence.append(n1)
            n1 *= coefficient
    index = random.randint(0,len(sequence)-1)
    missed_number = sequence[index]
    sequence[index] = "..."
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
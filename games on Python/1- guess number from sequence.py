from random import randint, choice
attempts = int(input("How many times you want to play? "))
for i in range(attempts):
    option = choice(["arithmetic", "geometric"]
    n1 = randint(1,10) # first element in sequence
    length = randint(5, 10) # length of sequence
    coefficient = randint(1, 5) # coefficient in sequence
    if option == "arithmetic":
        sequence = [n1 + i*coefficient for i in range(length)]
    else:
        sequence = [n1 * coefficient ** i for i in range(length)]

    index = randint(0, len(sequence)-1)  # index of missed number
    missed_number = sequence[index]
    sequence[index] = "..."
    print("Guess missed number: ")
    print(sequence)
    answer = int(input("Enter your answer: "))
    if answer != missed_number:
        print("You wrong!")
    else:
        print("You got it!")

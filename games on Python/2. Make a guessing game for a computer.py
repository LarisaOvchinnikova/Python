from random import randint
secret_number = int(input("Enter number in range 1-100 and computer will guess it: "))

low = 1
high = 100
count = 1
computer_guess = randint(low, high)
while computer_guess != secret_number:
    print(f"Computer think that it is {computer_guess}")
    result = int(input("Too big (1) or too small(2)? "))
    if result == 1:
        high = computer_guess - 1
    if result == 2:
        low = computer_guess + 1
    computer_guess = randint(low, high)
    count += 1
print(f"Your number is {computer_guess}. Took {count} guesses.")
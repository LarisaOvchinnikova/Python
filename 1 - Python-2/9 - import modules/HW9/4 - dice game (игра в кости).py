from random import randint
money = int(input("How much money in start of game? "))
computer_money = money
your_money = money
step = 0
while computer_money > 0 and your_money > 0:
    step += 1
    print(f"Round: {step}")
    bet = int(input("Enter bet: "))

    your_guess = int(input("Guess the roll: "))
    your_result = randint(1, 6) + randint(1, 6)

    computer_guess = randint(2, 12)
    computer_result = randint(1, 6) + randint(1, 6)

    print(f"YOU guessed {your_guess}, got {your_result}")
    print(f"Machine guessed {computer_guess}, got {computer_result}")

    if your_result == your_guess:
        your_money += bet
    else:
        your_money -= bet

    if computer_result == computer_guess:
        computer_money += bet
    else:
        computer_money -= bet

    print(f"Status: you have {your_money} euros, machine has {computer_money} euros")

if your_money > computer_money:
    print("YOU WIN!")
elif your_money < computer_money:
    print("MACHINE WIN")
else:
    print("DRAW!")
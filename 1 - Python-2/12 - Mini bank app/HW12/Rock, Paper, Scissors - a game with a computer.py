from random import choice
def rps(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()
    # rules = {
    #     "rock": "scissors",
    #     "scissors": "paper",
    #     "paper": "rock"
    # }
    rules = {
        "1": "3",
        "3": "2",
        "2": "1"
    }

    if rules[player1] == player2:
        return "You win!"
    elif player1 == player2:
        return "It is draw!"
    else:
        return "Machine win!"

print("------Welcome to the game of Rock, Paper, Scissors-----")
print()
times = int(input("How many round do you wish to play? "))
print("Okay, let's start...")
time = 0
your_score = 0
machine_score = 0
while time < times:
    time += 1
    print(f"Round {time}:")
    your_choice = input("Your choice Rock[1], Paper[2] or Scissors[3]? ")
    computer_choice = choice(["1", "2", "3"])
    result = rps(your_choice, computer_choice)
    if result == "You win!":
        your_score += 1
    elif result == "Machine win!":
        machine_score += 1

    if your_choice == "1":
        your_answer = "Rock"
    elif your_choice == "2":
        your_answer = "Paper"
    else:
        your_answer = "Scissors"

    if computer_choice == "1":
        computer_answer = "Rock"
    elif computer_choice == "2":
        computer_answer = "Paper"
    else:
        computer_answer = "Scissors"

    print(f"Your choice is {your_answer}, the machines choice is {computer_answer}. {result}!")
    print()
    print(f"The score - Player {your_score}:{machine_score} The Machine")
    print()

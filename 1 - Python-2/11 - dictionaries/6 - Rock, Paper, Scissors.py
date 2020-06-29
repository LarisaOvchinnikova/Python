# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
def rps(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if rules[player1] == player2:
        return "The winner is player1"
    elif player1 == player2:
        return "It is draw"
    else:
        return "The winner is player2"
print(rps("Rock", "Paper"))
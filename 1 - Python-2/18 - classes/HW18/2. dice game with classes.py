from random import randint

def computer_guess():
    return randint(2, 12)


def player_guess():
    try:
        res = int(input('Guess sum of number from two throws (2-12): '))
        return res
    except ValueError as e:
        print(e)
        return 0

def result_throw():
    return randint(1, 6) + randint(1, 6)

class Player:
    bet = 10

    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def result_message(self):
        return f"{self.name} guessed {self.guess}, got {self.result}"

    def game_loss(self):
        return self.capital <= 0

    def play_one_round(self):
        if self.name == "Computer":
            self.guess = computer_guess()
        else:
            self.guess = player_guess()

        self.result = result_throw()

        if self.guess == self.result:
            self.capital += Player.bet
        else:
            self.capital -= Player.bet

        print(self.result_message())


def play(nrounds, capital):
    you = Player('You', capital)
    computer = Player('Computer', capital)

    for step in range(1, nrounds + 1):
        print("Round:", step)
        try:
            new_bet = int(input("Enter the bet: "))
        except ValueError as e:
            print(e)
            continue
        Player.bet = new_bet
        you.play_one_round()
        computer.play_one_round()
        if you.game_loss() or computer.game_loss():
            break
        print(f"Status: {you.name} have {you.capital} dollars, {computer.name} has {computer.capital} dollars")

    if you.capital > computer.capital:
        print(f"{you.name} won!")
    elif you.capital < computer.capital:
        print(f"{computer.name} won!")
    else:
        print("Draw!")


play(10, 100)
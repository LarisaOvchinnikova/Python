from random import randint

def computer_guess():
    # All guesses have the same probability
    return randint(2, 12)


def player_guess():
    return int(input('Guess the sum of the number in the next throw: '))


def throw_dice():
    # TODO: функция возвращает результат броска двух кубиков от 1 до 6
    return randint(1, 6) + randint(1, 6)

class Player:
    bet = 10
    def __init__(self, name, capital, guess_function):
        self.name = name
        self.capital = capital
        self.guess_function = guess_function

    def message(self):
        # TODO: вернуть сообщение результата броска и попытки угадывания
        # Пример: Machine guessed 11, got 6
        # Или: YOU guessed 9, got 10
        return f"{self.name} guessed {self.guess}, got {self.result}"

    def broke(self):
        # TODO: проверить не проиграл ли еще игрок
        return self.capital < 0

    def play_one_round(self):
        # TODO: Создать действия одного раунда:
        # Игрок загадывает число
        self.guess = self.guess_function()
        # Игрок бросает кубики
        self.result = throw_dice()
        # Добавляет или отнимает ставку от капитала
        if self.guess == self.result:
            self.capital += Player.bet
        else:
            self.capital -= Player.bet
        # Печатает результат
        print(self.message())
        pass

def play(nrounds, capital):
    human = Player('You', capital, player_guess)
    computer = Player('Machine', capital, computer_guess)

    # Здесь основной цикл игры...
    for round in range(1, nrounds + 1):
        print("Round:", round)
        new_bet = int(input("Enter the bet: "))
        Player.bet = new_bet
        human.play_one_round()
        computer.play_one_round()
        if human.broke() or computer.broke():
            break
        print(f"Status: {human.name} have {human.capital} euros, {computer.name} have {computer.capital} euros")

    if human.capital > computer.capital:
        print(f"{human.name} won!")
    elif human.capital < computer.capital:
        print(f"{computer.name} won!")
    else:
        print("Draw!")


play(10, 100)


import random

class GuessNumber:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.number = random.randint(min_value, max_value)
        self.guesses = 0

    def get_guess(self):
        while True:
            guess = input(f"Try to guess number in range ({self.min_value}-{self.max_value})")
            if self.is_valid(guess):
                return int(guess)
            else:
                print("Wrong value! Try again!")

    def is_valid(self, str_number):
        try:
            num = int(str_number)
        except ValueError:
            return False
        return self.min_value <= num <= self.max_value

    def play(self):
        while True:
            guess = self.get_guess()
            self.guesses += 1
            if guess > self.number:
                print("Too big")
            elif guess < self.number:
                print("Too small")
            else:
                print(f"You got it. It took  you {self.guesses} attempts")
                break

for i in range (5):
    min_value = int(input("Enter min value: "))
    max_value = int(input("Enter max value: "))
    game = GuessNumber(min_value, max_value)
    game.play()
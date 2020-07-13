class TwoThreeNine:
    def __init__(self, number):
        self.number = number

    def twos(self):
        return self.number // 2

    def threes(self):
        return self.number // 3

    def nines(self):
        return self.number // 9


number1 = TwoThreeNine(23)
print(number1.twos())
print(number1.threes())
print(number1.nines())

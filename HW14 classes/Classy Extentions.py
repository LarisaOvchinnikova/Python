# https://www.codewars.com/kata/55a14aa4817efe41c20000bc/train/python
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f"{self.name} meows."
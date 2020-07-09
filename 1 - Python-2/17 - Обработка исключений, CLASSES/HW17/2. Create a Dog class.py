class Dog:
  height = 1
  weight = 1
  breed = ""
  barking = "Bark!"

  def bark(self):
    return self.barking

  def bmi(self):
    return self.weight / self.height ** 2

  def feed(self):
    return self.weight * 1.02

dog1 = Dog()
dog1.height = 0.5
dog1.weight = 5
dog1.breed = "Poodle"
dog1.barking = "Gav!! Gav!!"
print(f"{dog1.breed} says: {dog1.bark()}")
print(f"{dog1.breed} bmi is {dog1.bmi()}")
print(f"{dog1.breed} new weight is {dog1.feed()}")
print()
dog2 = Dog()
dog2.height = 0.5
dog2.weight = 20
dog2.breed = "Bulldog"
dog2.barking = "Bark!"

print(f"{dog2.breed} says: {dog2.bark()}")
print(f"{dog2.breed} bmi is {dog2.bmi()}")
print(f"{dog2.breed} new weight is {dog2.feed()}")

n = dog1.bmi()
while n < 25:
  dog1.weight = dog1.feed()
  n = dog1.bmi()

print(f"\nAfter feeding new {dog1.breed} bmi is {n}")
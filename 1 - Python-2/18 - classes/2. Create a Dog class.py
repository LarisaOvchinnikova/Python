class Dog:
  def __init__(self, height, weight, breed):
      self.height = height
      self.weight = weight
      self.breed = breed
      self.barking = "Bark!"

  def bark(self):
    return self.barking

  def bmi(self):
    return self.weight / self.height ** 2

  def feed(self):
    return self.weight * 1.02

dog1 = Dog(0.5, 5, "poodle")
dog1.barking = "Gav!! Gav!!"
print(dog1.bark())
print(dog1.bmi())
print(dog1.feed())

dog2 = Dog(0.5, 20, "Bulldog")
dog2.barking = "Bark!"

print(dog2.bark())
print(dog2.bmi())
print(dog2.feed())

n = dog1.bmi()
while n < 25:
  dog1.weight = dog1.feed()
  n = dog1.bmi()

print(dog1.bmi())
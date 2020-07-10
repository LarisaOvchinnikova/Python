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
print(dog1.bark())
print(dog1.bmi())
print(dog1.feed())

dog2 = Dog()
dog2.height = 0.5
dog2.weight = 20
dog2.breed = "Bulldog"
dog2.barking = "Bark!"

print(dog2.bark())
print(dog2.bmi())
print(dog2.feed())

n = dog1.bmi()
while n < 25:
  dog1.weight = dog1.feed()
  n = dog1.bmi()

print(dog1.bmi())
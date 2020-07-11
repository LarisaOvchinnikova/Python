# class Dog:
#     owner = "Jack"
#     weight = 15
#
# dog1 = Dog()
# dog2 = Dog()
# print(dog1.weight)   # 15
# print(dog1.weight)   # 15
#
# Dog.weight += 10  # поменяет атрибут класса
# print(Dog.weight)
# dog3 = Dog()
# dog4 = Dog()
# print(dog3.weight)   # 25
# print(dog4.weight)   # 25
#
# Dog.weight = 40
# print(dog1.weight)  #40
# print(dog2.weight)  #40
# print(dog1.weight)  #40
# print(dog2.weight)  #40  у всех вес изменился, так как это значение у переменной класса
#
# #чтобы все собаки были с разным весом
# # надо создать
# puppy1 = Dog()
# puppy1.weight = 12 #уникальный вес
# Dog.weight = 50
# print(puppy1.weight) # 12  -- не изменился
# print(dog1.weight)  #50
# print(dog2.weight)  #50
# --------------------------------------------
# print('------------------')
# class Dog:
#     owner = "Jack"
#
# puppy1 = Dog()
# puppy1.weight = 12
#
# puppy2 = Dog()
# puppy2.weight = 28
# print(puppy1.weight)
# print(puppy1.owner)
# print(puppy2.weight)
# print(puppy2.owner)
# puppy1.owner = "Jane"
# print(puppy1.owner)
# print(puppy2.owner)
# ==================================================
# Class / Instance variable
# конструктор класса def __init__
class Dog:
    def __init__(self, name, owner, weight):
        print(f"New puppy {name} here! Bark! with weight {weight}")
        self.weight = weight
        self.name = name
        self.owner = owner

    owner = "Jack"



puppy1 = Dog("Bonny", "Larisa", 5)
puppy2 = Dog("Jerry", "Anya", 4)
puppy3 = Dog("Julia", "Anya", 5)
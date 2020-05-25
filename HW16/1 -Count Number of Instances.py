# Создайте класс Dogs с возможностью посчитать количество cуществующих собак (instances).
# Записывайте это значение в атрибут dogs_count

class Dog:
    count = 0

    def __init__(self, name, breed):
        Dog.count += 1
        self.name = name
        self.breed = breed
        self.id = Dog.count
    def __repr__(self):
        return f"Dog('{self.name}', '{self.breed}', {self.id})"


pet1 = Dog("Elvis", "Retriever")
print(pet1.id)   # ---> 1
pet2 = Dog("Ghost", "Husky")
print(pet2.id)   # ---> 2
pet3 = Dog("Olaf", "Poodle")
print(pet3.id)   # ---> 3
list_of_dogs = [pet1,pet2,pet3]
print(list_of_dogs)
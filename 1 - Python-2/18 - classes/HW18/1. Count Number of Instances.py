class Dog:
    dogs_count = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.dogs_count += 1
        self.id = Dog.dogs_count

    def __str__(self):
        return f"Dog named {self.name}, breed {self.breed}, has id {self.id}"


pet1 = Dog("Elvis", "Retriever")
print(pet1.dogs_count)
pet2 = Dog("Ghost", "Husky")
print(pet2.dogs_count)
pet3 = Dog("Olaf", "Poodle")
print(pet3.dogs_count)

print(pet1)
print(pet2)
print(pet3)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, object):
        if self.age < object.age:
            return f"{object.name} is older than me."
        elif self.age > object.age:
            return f"{object.name} is younger than me."
        else:
            return f"{object.name} is the same age as me."


p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)

print(p1.compare_age(p2)) # ➞ "Joel is older than me."
print(p2.compare_age(p1)) # ➞ "Samuel is younger than me."
print(p1.compare_age(p3)) # ➞ "Lily is the same age as me."
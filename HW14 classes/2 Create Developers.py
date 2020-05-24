class Employee:
    def __init__(self, first_name, second_name, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.email = f"{first_name}.{second_name}@company.com"

    raise_rate = 1.05

    def full_name(self):
        return f"Hello, I'm {self.first_name} {self.second_name}"

    def apply_raise(self):
        self.salary += self.raise_rate

# наследник Employee:
class  Developers(Employee):
    def __init__(self, first_name, second_name, salary, language):
        super().__init__(first_name, second_name, salary)
        self.language = language
        self.raise_rate = 1.1

# emp1 = Employee("Jonh", "Doe", 100000)
# emp2 = Employee("Alice", "Moon", 150000)
dev1 = Developers("Victor", "Bogutski", 200000, "JS")
print(dev1.salary)
print(dev1.full_name())
print(dev1.email)
dev1.apply_raise()
print(dev1.salary)

class Employee:
    raise_rate = 1.05

    def __init__(self, first_name, second_name, salary):
        self.salary = salary
        self.second_name = second_name
        self.first_name = first_name
        self.email = f"{first_name}.{second_name}@company.com"

    def aplly_raise(self):
        self.salary *= self.raise_rate

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.first_name}", "{self.second_name}", {self.salary})'

    def __str__(self):
        return f"{self.first_name} {self.second_name} with salary --> {self.salary}"


class Developer(Employee):  # sub-class from Employee
        raise_rate = 1.1

        def __init__(self, first_name, last_name, salary, language):
            super().__init__(first_name, last_name, salary)
            self.language = language

        def __repr__(self):
            #    return f"Developer({self.first_name}, {self.last_name}, {self.salary}, {self.language}"
            return f"{self.__class__.__name__}({self.first_name}, {self.last_name}, {self.salary}, {self.language}"

emp1 = Employee("Jack", "Black", 100000)
emp2 = Employee("Lee", "Robertson", 700000)

dev1 = Developer("Bob", "Smith", 1400000, "Python")
dev2 = Developer("John", "Rich", 120000, "JS")

print(emp1)
print(emp2)

print(dev1)
print(dev2)
print(dev1.language)
print(dev1.raise_rate)
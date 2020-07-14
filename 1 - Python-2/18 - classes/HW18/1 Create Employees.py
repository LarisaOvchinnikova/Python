class Employee:
    raise_rate = 1.05
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name}.{last_name}@company.com"

    def apply_raise(self):
        #self.salary *= Employee.raise_rate
        self.salary *= self.raise_rate

    def __str__(self):
        return f"{self.first_name} {self.last_name} with salary ${self.salary}"


employee1 = Employee("Jack", "Black", 100000)
employee2 = Employee("Lee", "Robertson", 700000)
print(employee1)
print(employee2)
print(employee1.email)
print(employee2.email)
employee1.apply_raise()
employee2.apply_raise()
print(employee1.salary)
print(employee2.salary)
class Employee:
    raise_rate = 1.05
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name}.{last_name}@company.com"

    def apply_raise(self):
        self.salary *= self.raise_rate

    def __str__(self):
        return f"{self.first_name} {self.last_name} with salary ${self.salary}"

    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.salary}"



class Developer(Employee):  #sub-class from Employee
    raise_rate = 1.1

    def __init__(self, first_name, last_name, salary, language):
        super().__init__(first_name, last_name, salary)
        self.language = language

    def __repr__(self):
    #    return f"Developer({self.first_name}, {self.last_name}, {self.salary}, {self.language}"
        return f"{self.__class__.__name__}({self.first_name}, {self.last_name}, {self.salary}, {self.language}"


employee1 = Employee("Jack", "Black", 100000)
employee2 = Employee("Lee", "Robertson", 700000)

dev1 = Developer("Bob","Smith", 1400000, "Python")
dev2 = Developer("Ron","Smith", 5400000, "JS")
print(dev1)

#print(dir(dev1))

# все методы для девелопера наследуются оt employee
#or from  class object( )

print(isinstance(dev1, Employee)) # True
print(isinstance(employee1, Employee))  # True
print(isinstance(employee1, object))  # True
print(isinstance(dev1, object)) # True


# # object --->Employee --> Developer
#
# print(isinstance("hello", str)) #True
# print(isinstance("hello", object)) #True

print([dev1, dev2]) #[Employee(Bob, Smith, 1400000]
# после создания репрезентации дефелопера
#[Developer(Bob, Smith, 1400000, Python, Developer(Ron, Smith, 5400000, JS]
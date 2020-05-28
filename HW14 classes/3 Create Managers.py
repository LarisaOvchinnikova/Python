class Employee:
    def __init__(self, first_name, second_name, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.email = f"{first_name}.{second_name}@company.com"

    raise_rate = 1.05

    @property
    def full_name(self):
        return f"{self.first_name} {self.second_name}"

    def apply_raise(self):
        self.salary += self.raise_rate

    def __str__(self):
        return f"{self.first_name} {self.second_name} with salary --> {self.salary}"

    def __len__(self):
        return len(self.full_name)

    def __repr__(self):  # репрезентация объекта
        return f'{self.__class__.__name__}("{self.first_name}", "{self.second_name}", {self.salary})'

    def add_salary(self, object):
        return self.salary + object.salary

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary



class  Developer(Employee):
    def __init__(self, first_name, second_name, salary, language):
        super().__init__(first_name, second_name, salary)
        self.language = language
        self.raise_rate = 1.1


class Manager(Employee):
    def __init__(self, first_name, second_name, salary, employees_list):
        super().__init__(first_name, second_name, salary)
        self.employees_list = employees_list

    def remove_employee(self, employee):
        if employee in self.employees_list:
            self.employees_list.remove(employee)

    def add_employee(self, employee):
        if not employee in self.employees_list:
            self.employees_list.append(employee)

    def print_emps(self):
        for emp in self.employees_list:
            print(f"{emp.first_name} {emp.second_name} with salary --> {emp.salary}")

    def __len__(self):
        return len(self.employees_list)

emp1 = Employee("Jonh", "Doe", 100000)
emp2 = Employee("Alice", "Moon", 150000)
emp3 = Employee("Laura", "Sand", 50000)
dev1 = Developer("Victor", "Bogutski", 200000, "JS")
manager1 = Manager("Boss", "Manager", 300000, [emp1, emp2, emp3, dev1])

print(emp1)
print(len(emp1))

print(manager1.employees_list)
print(len(manager1))

# manager1.add_employee(emp3)
# print(manager1.employees_list)
#
# manager1.remove_employee(emp3)
# print((manager1.employees_list))
# manager1.add_employee(emp3)
#
# manager1.print_emps()
print(emp1.add_salary(emp3))  # работает функция add_salary

print(emp1 + emp2)  # работает функция __add__
print(emp1 - emp2)  # работает функция __sub__

print(emp1.full_name)

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


emp1 = Employee("Jonh", "Doe", 100000)
emp2 = Employee("Alice", "Moon", 150000)
emp3 = Employee("Laura", "Sand", 50000)
dev1 = Developer("Victor", "Bogutski", 200000, "JS")
manager1 = Manager("Boss", "Manager", 300000, [emp1, emp2, dev1])


print(manager1.employees_list)
manager1.add_employee(emp3)
print(manager1.employees_list)

manager1.remove_employee(emp3)
print((manager1.employees_list))
manager1.add_employee(emp3)

manager1.print_emps()

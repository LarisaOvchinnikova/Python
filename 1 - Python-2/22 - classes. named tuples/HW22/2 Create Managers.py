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
        return f"Employee ({self.first_name} {self.second_name} with salary --> {self.salary})"


class Developer(Employee):
    def __init__(self, first_name, second_name, salary, language):
        super().__init__(first_name, second_name, salary)
        self.language = language
        self.email = f"{first_name}.{second_name}@company.com"
        self.raise_rate = 1.1

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first_name}, {self.second_name}, {self.salary}, {self.language})"

    def __str__(self):
        return f"Developer({self.first_name} {self.second_name} with salary ---> {self.salary} and language {self.language})"

class Manager(Employee):
    def __init__(self, first_name, second_name, salary, employees_list):
        super().__init__(first_name, second_name, salary)
        self.email = f"{first_name}.{second_name}@company.com"
        self.employees_list = employees_list

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first_name}, {self.second_name}, {self.salary}, {self.employees_list})"

    def __str__(self):
        return f"Manager {self.first_name} {self.second_name} with salary --> {self.salary}, employeee list: {self.employees_list}"


    def add_employee(self, emp):
        if not emp in self.employees_list:
            self.employees_list.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees_list:
            self.employees_list.remove(emp)

    def print_emps(self):
        print("\nThe list of employees:")
        for emp in self.employees_list:
            print(f"{emp.first_name} {emp.second_name} with salary --> {emp.salary}")


emp1 = Employee("Jack", "Black", 100000)
emp2 = Employee("Lee", "Robertson", 700000)

dev1 = Developer("Bob", "Smith", 1400000, "Python")
dev2 = Developer("John", "Rich", 120000, "JS")

manager1 = Manager("Joe", "Martinez", 110000, [dev1, dev2, emp1])
print(manager1)
manager1.add_employee(emp2)
manager1.remove_employee(dev1)
manager1.print_emps()

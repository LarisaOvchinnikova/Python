# Создайте класс Employee в котором были бы атрибуты
# first_name, last_name, salary.
# На основе полученого имени внутри класса добавьте
# атрибут email: f"{first_name}.{second_name}@company.com"
# Cоздайте метод full_name(), который бы возвращал
# "Hello, I'm fullname"
# У всех работников должен быть атрибут raise_rate в 1.05
# Cоздайте метод apply_raise который бы повышал salary на raise_rate

class Employee:
    def __init__(self, first_name, second_name, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.salary = salary
        self.email = f"{first_name}.{second_name}@company.com"

    raise_rate = 1.05

    # def get_email(self):
    #     self.email = f"{self.first_name}.{self.second_name}@company.com"

    def raise_rate_update(self):
        self.raise_rate += 0.05

    def full_name(self):
        return f"Hello, I'm {self.first_name} {self.second_name}"

    def apply_raise(self):
        self.salary += self.raise_rate

emp1 = Employee("Jonh", "Doe", 100000)
print(emp1.full_name())

emp2 = Employee("Alice", "Moon", 150000)
# print(emp2.full_name())
# print(Employee.full_name(emp2))

# print(emp1.apply_raise())
# # print(emp1.salary)

emp1.apply_raise()
print(emp1.salary)

emp1.raise_rate_update()
print(emp1.raise_rate)
emp1.apply_raise()
print(emp1.salary)
# print(Employee.raise_rate)
# print(emp1.salary)
# print(emp2.salary)

# print(emp1.email)
# print(emp2.email)
#
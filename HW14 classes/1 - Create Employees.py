# Создайте класс Employee в котором были бы атрибуты
# first_name, last_name, salary.
# На основе полученого имени внутри класса добавьте
# атрибут email: f"{first_name}.{second_name}@company.com"
# Cоздайте метод full_name(), который бы возвращал
# "Hello, I'm fullname"
# У всех работников должен быть атрибут raise_rate в 1.05
# Cоздайте метод apply_raise который бы повышал salary на raise_rate

class Employee:
    # def __init__(self, first_name, second_name, salary):
    #     self.first_name = first_name
    #     self.second_name = second_name
    #     self.salary = salary
    raise_rate = 1.05
#emp1 = Employee("Jonh", "Doe", 100000)
emp1 = Employee()
emp2 = Employee()

#print(emp1)
print(emp1.raise_rate)
print(emp2.raise_rate)


Employee.raise_rate = 1.10  # изменение для всех объектов этого класса
print(emp1.raise_rate)
print(emp2.raise_rate)

emp1.raise_rate = 1.2   # изменение толко для этого объектв
print(emp1.raise_rate)
print(emp2.raise_rate)

# emp1 = Employee()
# print(emp1.raise_rate)      # 1.05
#
# emp1.raise_rate_update()
# print(emp1.raise_rate)   # 1.1
#
# emp1.raise_rate_update()
# print(emp1.raise_rate)   # 1.15
# emp1.raise_rate += 0.05  # 2-й способ
#
# emp2 = Employee()
# print(emp2.raise_rate)   # 1.05
#
# Employee.raise_rate_update(emp1)
# print(emp1.raise_rate)   # 1.1
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

#    def __str__(self):
#        return f"{self.first_name} {self.last_name} with salary ${self.salary}"

    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', {self.salary})"

emp1 = Employee("Jack", "Black", 100000)
emp2 = Employee("Lee", "Robertson", 700000)

employees = [emp1, emp2]
print(emp1) # Jack Black with salary $100000
print(employees)
#[<__main__.Employee object at 0x0036B100>, <__main__.Employee object at 0x0036B2E0>]

#  после метода репрезентации
# [Employee('Jack', 'Black', 100000), Employee('Lee', 'Robertson', 700000)]
# _str_ для печати объекта , __repr__ для списков объектов

# если _str_ убрать, то будет печать объекта с помощью repr

# # для репрезентации объекта
#

# from datetime import datetime
# day1 = datetime.today()
# day2 = datetime(2020, 10, 5, 14, 36, 15)
# print(day2) # 2020-10-05 14:36:15 --> репрезентация объекта
# print(day1) # 2020-07-15 22:50:29.858000
#
# days_list = [day1, day2]
# print(days_list)  # репрезентация объектов в модуле datetime
#
# print("Hello") # Hello  --> без кавычек(репрезентация
#
# x = '5'
# print(x)  # 5
# print(repr(x)) # '5'
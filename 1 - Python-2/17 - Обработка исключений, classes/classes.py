import math

class Circle:  # имя класса с большой буквы
    radius = 1  # attribute

    def area(self):
        return self.radius ** 2 * math.pi

class Rectangle:  # имя класса с большой буквы
    a = 1  # attribute
    b = 2
    def area(self):
        return self.a * self.b
    def perimeter(self):
        return (self.a + self.b) * 2
    def increase_a(self, amount):
        self.a += amount


my_circle1 = Circle()
print(my_circle1.radius)  #1
my_circle1.radius = 10
print(my_circle1.radius)   #2

my_circle2 = Circle()
print(my_circle2)  #<__main__.Circle object at 0x0070B268>
my_circle2.radius = 5

print(my_circle1.area())      # 314.1592653589793
print(Circle.area(my_circle1))# 314.1592653589793

print(my_circle2.area())      # 78.53981633974483


#===аналогия со строками и классом str
# print("hello".upper())
# print(str.upper("hello"))
#
# my_set = set()
# my_set.add(2)


r1 = Rectangle()
print(r1.area())  # 2

r1.a = 10
print(r1.area())
# r2 = Rectangle()
# r2.a = 5
# r2.b = 8
# print(r2.area())


r1.increase_a(2)
print(r1.a)
print(r1.area())

# class A:
# #     def __init__(self):
# #         pass
# #
# # obj1 = A()
# #
# #
# #
# # # for i in dir(A):
# # #     print(i)
# # #
# # # print(dir(list)) #список методов для класса
# #
# # # Dunder methods - double underscore
# # arr = [1,2,3]
# # # print(arr * 2) # [1, 2, 3, 1, 2, 3]
# # arr1 = [1,2,3]
# # arr2 = [4,5,6]
# # print(arr1 + arr2)
# # print(arr1.__add__(arr2))

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return self.radius ** 2 * 3.1415
#
#     def __add__(self, other):
#         return self.area() + other.area()
#
#     def __mul__(self, other):
#         return self.radius * other.radius
#
#     def __eq__(self, other):
#         return self.radius == other.radius
#
#     def __str__(self):
#         return f"Circle with radius {self.radius} "
#
#     def __repr__(self):
#         return f"Circle({self.radius})"
#
# circle1 = Circle(10)
# circle2 = Circle(10)
# print(circle1.area())
# print(circle2.area())
# print(circle1 + circle2)
# print(circle1.__add__(circle2))
# print(circle2 * circle1)
# print(circle1 == circle2)
#
# # print(dir(Circle))
# print(str(circle1))
# print(circle1)
#
# iolution:
# 1
# def alphabet_war(fight):
#
print(dir(str))
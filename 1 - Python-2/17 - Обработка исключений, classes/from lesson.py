# x = float("18,4") #ValueError: could not convert string to float: '18,4'
# print(x)

# обработка ошибок в блоке try except
# while True:
#     try:
#         day = input("Enter the day: ")
#         day = int(day)
#         break
#     except:
#         print("You entered the wrong input")
#
# print("Today is", day)
# -------
# def div(x, y):
#     return x / y
#
# try:
#     print(div(10, 0))
# except:
#     print("Cannot divide by zero!")
# ==========================================

# name = input("Enter the name of the file: ")
# try:
#     file = open(name)
# except:
#     print("No such file!")
#     quit()  # дальше команды не будут выполняться
#
# print("Next")  # эта команда не выполнится в случае если файла нет

# ---------------------------------------
# try:
#     x = 10
#     y = int(input("Enter the y: "))
#     print(x / y)
# except:
#     #pass  # пропустит ошибку и дальше код работает
# ============================================
# try:
#     x = 10
#     y = int(input("Enter the y: "))
#     print(x / y)
#    # print(z)
# except ValueError as e:
#     print("Integer required")
#     print(e)
# except ZeroDivisionError as e:
#     print("Must not be zero!")
#     print(e)
# except Exception as error:  #поймает все ошибки которые не обнаружены ранее
#     print(error)
# finally:              #выполняется всегда и после ошибок и без
#     print("Good bye friend")
#     quit()
#===================
# f = open("test.txt", "w")
# try:
#     f.write("Hello")
#     y = 1/0
# except Exception as e:
#     print(e)
#
# finally:
#     f.close()
#     print("File is closed", f.closed)

# =======================

# with open("test.txt", "w") as f:  # открывает файл, записывает его в f
# # и автоматически закрывает файл
#     print(f)  # объект - ссылка на файл
#     f.write("Hi")
#
# print("File is closed", f.closed)
# print

# ========================================
# Classes and OOP
# Functions
# input ---> Function ---> output
#
# string, integer, float,list - objects
# All objects have a type
# print(type("Hello")) ---> <class str>
#Objects are bits of code and data
# у строк есть методы,
#объекты создаются с помощью классов

# Class is an extensible program-code-template for creating objects
# Instance - an individual object of a certain class
# Attributes - a bit of data in a class
 # Methods are functions that live inside class


def factorial(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

# print(factorial(4) == 24)
# print(factorial(10))

# if factorial(4) == 24:
#     print("factorial(4) works good")
# else:
#     print("Wrong")
#
# if factorial(5) == 120:
#     print("factorial(5) works good")
# else:
#     print("Wrong")


def check(tested_value, exact_value):
    tested_value = factorial(tested_value)
    if tested_value == exact_value:
        return "Ok"
    else:
        return f"{tested_value} doesnt equal {exact_value}"


print(check(5, 120))  # Ok
print(check(4, 24))   # Ok

assert factorial(5) == 120
assert factorial(3) == 6

# установка Pytest для тестирования
# в терминале пишем :
# pip install pytest

# для запуска надо после написания теста  в терминале писать pytest

# для запуска только одного файла
# pytest first.py

print(__name__)   # __main__

if __name__ == "__main__":
    print("Hello")
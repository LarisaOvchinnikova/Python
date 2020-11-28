days = 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()

print(days)
print(sorted(days, key=len)) # sort by length of words


days = [('Monday', 'Chest+biceps', '45'),
        ('Tuesday', 'Back+triceps', '45'),
        ('Wednesday', 'Core', '30'),
        ('Thursday', 'Legs', '55'),
        ('Friday', 'Shoulders', '45'),
        ('Saturday', 'Rest', '0'),
        ('Sunday', 'Rest', '0')]

def get_third(element):
    return element[2]

print(sorted(days,key=get_third))   # сортировка по посл.элементу таплс

def get_second(element):
    return element[1]

print(sorted(days,key=get_second))   # сортировка по 2 элементу таплс

# Анонимные функции могут содержать лишь одно выражение,
# но и выполняются они быстрее. Анонимные функции создаются
# с помощью инструкции lambda. Кроме этого, их не обязательно
# присваивать переменной, как делали мы инструкцией def func():
# func = lambda x, y: x + y
# func(1, 2) # 3
# func('a', 'b') # 'ab'
# (lambda x, y: x + y)(1, 2) # 3
# (lambda x, y: x + y)('a', 'b') #  ab'
# lambda функции, в отличие от обычной,
не требуется инструкция return, а в остальном,
ведет себя точно так же:
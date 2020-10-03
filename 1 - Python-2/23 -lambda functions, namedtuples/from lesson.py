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

print(sorted(days,key=get_third,r))   # сортировка по посл.элементу таплс

def get_second(element):
    return element[1]

print(sorted(days,key=get_second))   # сортировка по 2 элементу таплс



import random

def gen_sequence():
    """ Эта функция генерирует случайный список из чисел от 1 до 10
    Пропуская одну случайную цифру, используйте для своих проверок"""
    return random.sample(range(1, 11), 9)


def find_missing(arr):
    """Ваша функция чтобы найти пропущенное число из списка"""
    full = set(range(1,11))
    return list(full - set(arr))[0]


arr = gen_sequence()
print(arr)
print(find_missing(arr))
import datetime
from datetime import date, timedelta
from random import randint, sample


def gen_dates_list():
    """Ваша функция чтобы сгенерировать случайный список из дат"""
    today = date.today() + timedelta(randint(-100, 100))
    dates = [today + timedelta(i) for i in range(randint(15, 25))]
    return sample(dates, randint(10, 15))


dates_list = gen_dates_list()
print(dates_list)
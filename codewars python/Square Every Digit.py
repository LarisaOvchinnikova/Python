def square_digits(num):
    a = [str(int(el)**2) for el in str(num)]
    return int("".join(a))
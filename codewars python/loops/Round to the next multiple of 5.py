https://www.codewars.com/kata/55d1d6d5955ec6365400006d
def round_to_next5(n):
    if n % 5 == 0:
        return n
    else:
        return (n - n % 5) + 5
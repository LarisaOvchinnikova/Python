https://www.codewars.com/kata/596f6385e7cd727fff0000d6
def avg_array(arrs):
    return [sum(a)/len(a) for a in zip(*arrs)]
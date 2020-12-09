# https://www.codewars.com/kata/59619e4609868dd923000041
def total_bill(s):
    n = s.count('r')
    free = n // 5
    return (n - free) * 2